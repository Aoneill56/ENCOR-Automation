# EtherChannel / LACP

EtherChannel combines physical links into one logical Port-channel.

## LACP modes

- `active` — initiates negotiation
- `passive` — responds to negotiation

Working combinations:

```text
active + active
active + passive
```

Normally not:

```text
passive + passive
```

## Configuration

```cisco
interface range Ethernet0/1-2
 channel-group 1 mode active
 no shutdown
```

Configure the logical interface:

```cisco
interface Port-channel1
 switchport mode trunk
 switchport trunk allowed vlan 10-20,40
```

Verify:

```cisco
show etherchannel summary
show lacp neighbor
show interfaces Port-channel1
show interfaces trunk
```

## Troubleshooting

Compare both physical members:

```cisco
show run interface Ethernet0/1
show run interface Ethernet0/2
```

Check:

- Physical state
- LACP mode
- Switchport mode
- Allowed VLANs
- Native VLAN
- Speed/duplex where applicable
- Peer configuration

If members are suspended or individual, investigate before assuming the Port-channel works.
