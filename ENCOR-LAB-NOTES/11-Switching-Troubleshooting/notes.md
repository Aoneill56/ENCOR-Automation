# Switching Troubleshooting

Use a Layer-by-Layer approach.

## Layer 1

```cisco
show interfaces status
show interfaces counters errors
show interfaces Ethernet0/1
```

Check link state, errors, speed, duplex and flaps.

## Layer 2

```cisco
show vlan brief
show interfaces trunk
show interfaces Ethernet0/1 switchport
```

Check VLAN existence, access VLAN, trunk mode, allowed VLANs and native VLAN.

## STP

```cisco
show spanning-tree
show spanning-tree root
show spanning-tree vlan 10
```

Check root, role, state and topology.

## EtherChannel

```cisco
show etherchannel summary
show lacp neighbor
```

Check whether members are actually bundled.

## Layer 3

```cisco
show ip interface brief
show ip route
show arp
```

Check interfaces, routes and ARP.

## Practical decision tree

```text
Physical link
    ↓
Interface up/up?
    ↓
Correct switchport mode?
    ↓
VLAN exists?
    ↓
VLAN allowed on trunk?
    ↓
STP forwarding?
    ↓
Correct IP/subnet?
    ↓
ARP?
    ↓
Routing?
    ↓
Ping / traceroute
```

Do not jump directly to routing if Layer 1 or Layer 2 has not been verified.

## Configuration vs operational state

```cisco
show running-config
```

shows configuration.

Operational commands such as:

```cisco
show interfaces trunk
show spanning-tree
show etherchannel summary
```

show what the network is actually doing.

Always verify both.
