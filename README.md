# meraki-switchports-backup

Small script to backup and restore `Meraki MS` switch port configurations, which can be used to easily replace a switch.

Original: https://github.com/itris-one/meraki-interface-backup

Changed to use the new [Meraki Dashboard API](https://github.com/meraki/dashboard-api-python). 

#### Setup of dependencies
`python3 -m pip install -r requirements.txt`

#### Example
```
python3 backup.py -k [api-key] backup
python3 backup.py -k [api-key] -f "name=SWITCH007" restore
```

### Example of backup contents

<details>
  <summary>Below is the backup of MS120-48</summary>

```json
[
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "1",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "2",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "3",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "4",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "5",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "6",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "7",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "8",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "9",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "10",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "11",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "12",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "13",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "14",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "15",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "16",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "17",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "18",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "19",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "20",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "21",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "22",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "23",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "24",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "25",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "26",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "699746792102691463",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "access",
      "udld": "Alert only",
      "vlan": 43,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "27",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "28",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "29",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "30",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "31",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "32",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "33",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "34",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "35",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "36",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "37",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "38",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "39",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "40",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "41",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "42",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "43",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "44",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "45",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "46",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "47",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)",
         "100 Megabit (auto)",
         "100 Megabit half duplex (forced)",
         "100 Megabit full duplex (forced)",
         "10 Megabit (auto)",
         "10 Megabit half duplex (forced)",
         "10 Megabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "48",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "49",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "50",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "51",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   },
   {
      "accessPolicyType": "Open",
      "allowedVlans": "all",
      "daiTrusted": false,
      "enabled": true,
      "isolationEnabled": false,
      "linkNegotiation": "Auto negotiate",
      "linkNegotiationCapabilities": [
         "Auto negotiate",
         "1 Gigabit full duplex (forced)"
      ],
      "mirror": {
         "mode": "Not mirroring traffic"
      },
      "module": {
         "model": null
      },
      "name": null,
      "poeEnabled": false,
      "portId": "52",
      "portScheduleId": null,
      "profile": {
         "enabled": false,
         "id": "",
         "iname": null
      },
      "rstpEnabled": true,
      "schedule": null,
      "stpGuard": "disabled",
      "tags": [],
      "type": "trunk",
      "udld": "Alert only",
      "vlan": 1,
      "voiceVlan": null
   }
]
```
</details>
