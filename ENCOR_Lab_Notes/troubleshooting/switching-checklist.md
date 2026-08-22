# Switching Troubleshooting Checklist

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

Check:

- VLAN exists
- access/trunk mode
- access VLAN
- trunk operational state
- allowed VLANs
- native VLAN

## STP

```cisco
show spanning-tree
show spanning-tree root
show spanning-tree vlan 10
show spanning-tree interface Ethernet0/1 detail
```

Check root, port role, state and unexpected topology.

## EtherChannel

```cisco
show etherchannel summary
show lacp neighbor
```

Check whether members are actually bundled.

## Layer 3 / SVI

```cisco
show ip interface brief
show ip route
show arp
```

Check SVI state, IP address, routing and ARP.

## Practical sequence

If SW1 cannot ping a router:

```text
1. Is the physical link up?
2. Is the switch port the expected mode?
3. Does the VLAN exist?
4. Is the VLAN allowed across the trunk?
5. Is the native VLAN correct?
6. Is STP forwarding?
7. Does the router interface have the expected IP?
8. Is the router interface up/up?
9. Is ARP resolving?
10. Only then investigate routing.
```

## Automation verification

```text
Configure
   ↓
show interfaces trunk
   ↓
show vlan brief
   ↓
show spanning-tree
   ↓
show etherchannel summary
   ↓
show ip interface brief
   ↓
ping / application test
```

Automation is not finished when Ansible reports `changed`; it is finished when the resulting device state is verified.
