# VLANs and Trunks

## VLAN configuration

```cisco
conf t
vlan 10
 name USERS
vlan 20
 name SERVERS
vlan 30
 name VOICE
vlan 40
 name MANAGEMENT
end
```

Verify:

```cisco
show vlan brief
```

## Access port

```cisco
interface Ethernet0/10
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
```

## Voice Vlan

```cisco
interface Ethernet0/10
 switchport voice vlan 30
 no shutdown
```

Verify:

```cisco
show interfaces Ethernet0/10 switchport
show vlan brief
```

## Trunk

```cisco
interface Ethernet0/1
 switchport mode trunk
 switchport trunk native vlan 1
 switchport trunk allowed vlan 10-20,40
 no shutdown
```

Verify:

```cisco
show interfaces trunk
show interfaces Ethernet0/1 switchport
```

## Troubleshooting

If VLAN 10 works locally but not across a trunk:

1. Does VLAN 10 exist?
2. Is the trunk operational?
3. Is VLAN 10 allowed?
4. Does the native VLAN match?
5. Is STP forwarding VLAN 10?

Useful commands:

```cisco
show vlan brief
show interfaces trunk
show interfaces Ethernet0/1 switchport
show spanning-tree vlan 10
```
