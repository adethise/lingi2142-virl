telnet_ip = '172.16.11.254'

# ROUTER NAMES
C1      = "C1"
C2      = "C2"
C3      = "C3"
E1      = "E1"
E2      = "E2"
E3      = "E3"
EXT1    = "EXT1"
EXT2    = "EXT2"
EXT3    = "EXT3"

# INTERFACE DIRECTIONS
SOUTH   = "SOUTH"
NORTH   = "NORTH"
EAST    = "EAST"
WEST    = "WEST"
NW  = "NW"
NE  = "NE"
SW  = "SW"
SE  = "SE"

############################
# PORT CHANGE AT EACH STARTUP AND SHOULD UPDATED
############################
telnet_ports = {
    C1:   17005,
    C2:   17003,
    C3:   17000,
    E1:   17007,
    E2:   17011,
    E3:   17009,
    EXT1: 17017,
    EXT2: 17015,
    EXT3: 17017
}

# LOOPBACK IPS
loopback_ips = {
    C1:   '192.168.0.2',
    C2:   '192.168.0.3',
    C3:   '192.168.0.6',
    E1:   '192.168.0.1',
    E2:   '192.168.0.4',
    E3:   '192.168.0.5',
    EXT1: '192.168.0.7',
    EXT2: '192.168.0.9',
    EXT3: '192.168.0.13'
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
        NORTH:   '10.0.0.1',
        SE:      '10.0.0.6'
    },
    E2: {
        NW:      '10.0.0.10',
        NE:      '10.0.0.22',
        SW:      '10.0.0.25'
    },
    E3: {
        NORTH:   '10.0.128.5',
        WEST:    '10.0.128.10',
        SW:      '10.0.0.30'
    },
    EXT1: {
        SOUTH:   '10.0.0.2'
    },
    EXT2: {
        SOUTH:   '10.0.128.6'
    },
    EXT3: {
        EAST:   '10.0.0.26'
    }
}
