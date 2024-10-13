import argparse
import os
import logging as log
import json
import re

import meraki


def filter_devices(device_list, key, val, case_sensitive=True):
    if not case_sensitive:
        val = val.lower()

    for device_item in device_list:
        if device_item.get(key) == val:
            yield device_item
        elif device_item.get(key, "").lower() == val and not case_sensitive:
            yield device_item


def zerowidthsplit(pattern, string):
    splits = list(m.start() for m in re.finditer(pattern, string))
    starts = [0] + splits
    ends = splits + [ len(string) ]
    return [string[start:end] for start, end in zip(starts, ends)]


def convertPortObject(port):
    """Converts the port object to make it compatible with the Update Switch Port API Call"""
    new_port = {}
    camelCase = re.compile(r'(?<=[a-z])(?=[A-Z])')

    for k, v in port.items():
        if k == "":
            continue

        k = zerowidthsplit(r'(?<=[a-z])(?=[A-Z])', k)
        new_key = "_".join(k).lower()
        new_port[new_key] = v

    new_port["mtype"] = new_port["type"]
    del new_port["type"], new_port["number"]
    new_port["storm_control_enabled"] = None

    return new_port


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Small python script for backup and restore of meraki port configs.
    Example: backup.py -k MERAKI_API_KEY
    Exmaple: backup.py -k MERAKI_API_KEY restore "name=sw01"
""")

    parser.add_argument('-k', '--api-key', help='Meraki API Key (X-Cisco-Meraki-API-Key)', default=os.environ.get("MERAKI_API_KEY"))
    parser.add_argument('-v', '--verbose', action='store_const', const=True, help='verbose mode')
    parser.add_argument('-f', '--filter', help='filter devices (restore only, mandatory) "name=sw01" or "serial=ABCD-EFGH-IJKLM"')
    parser.add_argument('-i', '--org-id', help='Organization ID (optional if only one organization assigned)')

    parser.add_argument('action', nargs="?", default="backup", help='backup or restore (default backup)')
    parser.add_argument('path', nargs="?", help='(re)store backups (from) here (default: backup_orgid)')

    args = parser.parse_args()

    if args.verbose:
        log.basicConfig(level=log.DEBUG)

    if not args.api_key:
        parser.print_help()
        exit(1)

    dashboard = meraki.DashboardAPI(args.api_key)
    organizationID = args.org_id

    if not organizationID:
        log.info("No Organization ID provided, I try to find one")
        organizations = dashboard.organizations.get_organizations()
        if len(organizations) != 1:
            print("API Token has access to no or more than one organization, please provide a organization id")
            print(organizations)
            exit(1)
        else:
            organizationID = organizations[0]["id"]

    backup_dir = args.path

    if backup_dir is None:
        backup_dir = "backup_%s" % organizationID

    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)

    log.info("Organization ID is %s" % organizationID)

    if args.action == "backup":
        print("requesting devices")
        devices = dashboard.organizations.getOrganizationDevices(organizationId=organizationID)
        print(" - Found %s devices in organization" % len(devices))

        with open(os.path.join(backup_dir, "_devices.json"), "w") as devices_json:
            devices_json.write(json.dumps(devices, indent=3, sort_keys=True))

        for device in devices:
            model = device["model"]

            if model.startswith("MS"): # Filter meraki switches
                print("Portconfig Backup of '%(name)s'(%(serial)s)" % device)
                serial = device["serial"]

                with open(os.path.join(backup_dir, "%s_ports.json" % serial), "w") as config:
                    config.write(json.dumps(dashboard.switch.getDeviceSwitchPorts(serial), indent=3, sort_keys=True))

            else:
                print("Skipping '%(name)s'(%(serial)s)" % device)
    elif args.action == "restore":
        device_filter = args.filter
        if not device_filter:
            parser.print_help()
            exit(1)

        filter_key, filter_value = device_filter.split("=")
        filter_key, filter_value = filter_key.lower().strip(), filter_value.strip()

        case_sensitive = True
        if filter_key == "name":
            case_sensitive = False

        log.info("Device filter key %s value %s" % (filter_key, filter_value))

        local_devices = json.load(open(os.path.join(backup_dir, "_devices.json"), "r"))
        local_devices = list(filter_devices(local_devices, filter_key, filter_value, case_sensitive))
        log.info("Matched %s devices in backup folder" % len(local_devices))

        cloud_devices = dashboard.organizations.getOrganizationDevices(organizationId=organizationID)
        cloud_devices = list(filter_devices(cloud_devices, filter_key, filter_value, case_sensitive))

        log.info("Matched %s devices on cloud controller" % len(cloud_devices))

        if len(cloud_devices) != 1 and len(local_devices) != 1:
            log.error("Device not found, unknown device or invalid device filter")
            exit(1)

        local_device = local_devices[0]
        cloud_device = cloud_devices[0]
        serial = local_device["serial"]

        log.info("found device local and on cloud controller")

        print("Restore port configuration of '%(name)s'(%(serial)s)" % local_device +
              " cloud: '%(name)s'(%(serial)s)" % cloud_device)

        log.info("Load Port configuration of '%(name)s'(%(serial)s)" % local_device)

        device_ports = json.load(open(os.path.join(backup_dir, "%s_ports.json" % serial), "r"))
        print(" - Found %s ports" % len(device_ports))

        for port in device_ports:
            print(" - restoring port %(portId)s (%(name)s)" % port)
            # print(port)
            dashboard.switch.updateDeviceSwitchPort(serial=cloud_device["serial"], **port)
        
