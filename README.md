# meraki-interface-backup
Small script which backups the interface configuration of an switch. It can be used to easily replace an switch.

#### Setup of dependencies
`python3 -m pip install -r requirements.txt`

#### Example
```
python3 backup.py -k [api-key] backup
python3 backup.py -k [api-key] -f "name=SWITCH007" restore
```
