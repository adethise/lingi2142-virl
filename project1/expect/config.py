telnet_ip = '172.16.11.254'

# ROUTER NAMES
C1      = 'C1'
C2      = 'C2'
C3      = 'C3'
E1      = 'E1'
E2      = 'E2'
E3      = 'E3'
EXT1    = 'Ext1'
EXT2    = 'Ext2'
EXT3    = 'Ext3'

# INTERFACE DIRECTIONS
SOUTH   = 'SOUTH'
NORTH   = 'NORTH'
EAST    = 'EAST'
WEST    = 'WEST'
NW  = 'NW'
NE  = 'NE'
SW  = 'SW'
SE  = 'SE'

core_routers = [C1, C2, C3]

####################################################
# PORT CHANGE AT EACH STARTUP AND SHOULD UPDATED   #
####################################################
telnet_ports = {
    C1:   17036,
    C2:   17040,
    C3:   17038,
    E1:   17052,
    E2:   17050,
    E3:   17048,
    EXT1: 17042,
    EXT2: 17046,
    EXT3: 17044
}

# LOOPBACK IPS
loopback_ips = {
    C1:   '192.168.0.1',
    C2:   '192.168.0.2',
    C3:   '192.168.0.3',
    E1:   '192.168.0.4',
    E2:   '192.168.0.5',
    E3:   '192.168.0.6',
    EXT1: '192.168.1.1',
    EXT2: '192.168.2.1',
    EXT3: '192.168.3.1'
}

# EXTERNAL ADVERTISED PREFIXES
external_ips = {
    EXT1:           '10.1.1.1',
    EXT2:           '10.2.1.1',
    EXT3:           '10.3.1.1',
    EXT1+EXT2+EXT3: '10.4.1.1',
    EXT1+EXT2:      '10.7.1.1',
    EXT2+EXT3:      '10.6.1.1',
    EXT1+EXT3:      '10.5.1.1'
}

# INTEFACE IPS
interface_ips = {
    C1: {
        NE:     '10.0.0.17',
        EAST:   '10.0.0.13',
        SE:     '10.0.0.9',
        NW:     '10.0.0.5'
    },
    C2: {
        NW:     '10.0.128.1',
        NE:     '10.0.0.29',
        SW:     '10.0.0.21',
        WEST:   '10.0.0.14'
    },
    C3: {
        EAST:    '10.0.128.9',
        SE:      '10.0.128.2',
        SW:      '10.0.0.18'
    },
    E1: {
        NORTH:   '10.1.0.2',
        SE:      '10.0.0.6'
    },
    E2: {
        NW:      '10.0.0.10',
        NE:      '10.0.0.22',
        SW:      '10.2.0.2'
    },
    E3: {
        NORTH:   '10.3.0.2',
        WEST:    '10.0.128.10',
        SW:      '10.0.0.30'
    },
    EXT1: {
        SOUTH:   '10.1.0.1'
    },
    EXT2: {
        EAST:    '10.2.0.1'
    },
    EXT3: {
        SOUTH:   '10.3.0.1'
    }
}
