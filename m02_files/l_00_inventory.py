inventory = [
    {
        "name": "devnet-csr-always-on-sandbox",
        "ssh-info": {
            "hostname": "ios-xe-mgmt-latest.cisco.com",
            "port": 8181,
            "credentials": {"username": "developer", "password": "Cisco12345"},
            "device_type": "cisco_ios",
        },
        "netconf-info": {"port": 10000},
        "restconf-info": {"port": 9443},
    },
    {
        "name": "devnet-csr-always-on-sandbox",
        "ssh-info": {
            "hostname": "sbx-nxos-mgmt.cisco.com",
            "port": 8181,
            "credentials": {"username": "admin", "password": "Admin_1234!"},
            "device_type": "cisco_nxos",
        },
    },

]

csv_inventory = [
    ["name", "hostname", "ssh-port", "ssh-username", "ssh-password"],
    [
        "devnet-csr-always-on-sandbox",
        "ios-xe-mgmt-latest.cisco.com",
        "8181",
        "developer",
        "Cisco12345",
    ],
    [
        "devnet-csr-always-on-sandbox",
        "sbx-nxos-mgmt.cisco.com",
        "8181",
        "admin",
        "Admin_1234!",
    ],
]

xml_inventory = {
    "inventory": {
        "devices": [
            {
                "name": "devnet-csr-always-on-sandbox",
                "ssh-info": {
                    "hostname": "ios-xe-mgmt-latest.cisco.com",
                    "port": "8181",
                    "credentials": {"username": "developer", "password": "Cisco12345"},
                    "device_type": "cisco_ios",
                },
                "netconf-info": {"port": "10000"},
                "restconf-info": {"port": "9443"},
            },
            {
                "name": "devnet-csr-always-on-sandbox",
                "ssh-info": {
                    "hostname": "sbx-nxos-mgmt.cisco.com",
                    "port": "8181",
                    "credentials": {"username": "admin", "password": "Admin_1234!"},
                    "device_type": "cisco_nxos",
                },
            }
        ]
    }
}
