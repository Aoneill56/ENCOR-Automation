# SVI and Inter-VLAN Routing

An SVI provides a Layer-3 interface associated with a VLAN.

## Configure

```cisco
vlan 10
 name USERS

interface Vlan10
 ip address 192.168.10.1 255.255.255.0
 no shutdown
```

For another VLAN:

```cisco
vlan 20
 name SERVERS

interface Vlan20
 ip address 192.168.20.1 255.255.255.0
 no shutdown
```

Verify:

```cisco
show ip interface brief
show interfaces Vlan10
show interfaces Vlan20
```

## Troubleshooting SVI down

Check:

```cisco
show vlan brief
show spanning-tree vlan 10
show interfaces trunk
show ip interface brief
```

An SVI may remain down if the VLAN does not have an active Layer-2 path.

## Inter-VLAN test

From a host in VLAN 10:

```text
192.168.10.x
gateway 192.168.10.1
```

Test the gateway first, then a host in VLAN 20.

```text
Host → SVI gateway → routing → destination VLAN
```

## CML lab

Create VLANs 10 and 20, assign access ports, create SVIs, and verify that hosts in different VLANs can communicate through the Layer-3 switch.
