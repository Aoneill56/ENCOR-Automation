# Multiple Spanning Tree (MST)

MST (802.1s) maps multiple VLANs to a smaller number of spanning-tree instances.

## MST region

Switches belong to the same MST region only when these match:

- Region name
- Revision number
- VLAN-to-instance mapping

Example:

```cisco
spanning-tree mst configuration
 name CAMPUS
 revision 1
 instance 1 vlan 10-20
 instance 2 vlan 30-40
 exit
```

Verify:

```cisco
show spanning-tree mst configuration
```

A mismatch can create an MST boundary.

## Instances

Example:

```text
MST 1 -> VLANs 10-20
MST 2 -> VLANs 30-40
```

You can deliberately place different switches as roots for different instances:

```cisco
spanning-tree mst 1 priority 24576
spanning-tree mst 2 priority 28672
```

Another switch can use the reverse priorities to balance paths.

## Verification

```cisco
show spanning-tree mst
show spanning-tree mst configuration
show spanning-tree mst 1
show spanning-tree mst 2
```

## MST troubleshooting

1. Check region name.
2. Check revision.
3. Check VLAN-to-instance mapping.
4. Check root placement.
5. Check trunk VLANs.
6. Check for an MST boundary.
7. Check instance roles and states.

## CML lab

Three switches in a triangle:

```text
        SW1
       /   \
     SW2---SW3
```

Map VLANs 10-20 to MST 1 and VLANs 30-40 to MST 2. Make SW1 root for instance 1 and SW2 root for instance 2.
