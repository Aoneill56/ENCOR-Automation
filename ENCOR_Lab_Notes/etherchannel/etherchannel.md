# EtherChannel / Port-Channel

EtherChannel bundles physical links into one logical interface. LACP is the common standards-based negotiation protocol.

## LACP modes

- `active` — actively negotiates.
- `passive` — responds to LACP but does not initiate.

A channel can form with:

`active + active`

or:

`active + passive`

`passive + passive` does not normally form.

## Example

```cisco
interface range Ethernet0/1-2
 channel-group 1 mode active
```

Then configure the logical interface:

```cisco
interface Port-channel1
 switchport mode trunk
 switchport trunk allowed vlan 10-20,40
```

Verify:

```cisco
show etherchannel summary
show lacp neighbor
show interfaces port-channel 1
show interfaces trunk
```

## Member consistency

Members need compatible settings, including:

- switchport mode
- native VLAN
- allowed VLANs
- speed/duplex where applicable
- channel protocol/mode

## Troubleshooting

```cisco
show etherchannel summary
show lacp neighbor
show interfaces status
show run interface Ethernet0/1
show run interface Ethernet0/2
show run interface Port-channel1
```

Look for suspended, individual or non-bundled members.

## Automation

Ansible can configure Port-Channels and member interfaces, but exact module/model support depends on the platform. Always verify the resulting state.
