# VLANs and Trunks

## Create VLANs

```cisco
vlan 10
 name USERS

vlan 20
 name SERVERS

vlan 40
 name MANAGEMENT
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
```

## Trunk

```cisco
interface Ethernet0/1
 switchport mode trunk
 switchport trunk native vlan 1
 switchport trunk allowed vlan 10-20,40
```

Verify:

```cisco
show interfaces trunk
show interfaces Ethernet0/1 switchport
```

## Native VLAN

The native VLAN carries untagged traffic on an 802.1Q trunk. Both ends should agree on the native VLAN.

## Allowed VLANs

A VLAN can exist on a switch but still fail across a trunk if it is not allowed.

Always check:

```cisco
show interfaces trunk
```

## SVI

```cisco
interface Vlan10
 ip address 192.168.10.1 255.255.255.0
 no shutdown
```

Verify:

```cisco
show ip interface brief
show interfaces vlan 10
```

For an SVI to be operational, the VLAN generally needs to exist and have an active Layer-2 path.
