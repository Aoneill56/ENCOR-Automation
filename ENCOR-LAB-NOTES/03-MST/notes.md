# Multiple Spanning Tree — MST

MST (802.1s) maps multiple VLANs to a smaller number of spanning-tree instances.

## MST region

These must match:

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

Enable MST:

```cisco
spanning-tree mode mst
```

Verify:

```cisco
show spanning-tree mst configuration
show spanning-tree mst
```

## Root placement

Example:

```cisco
spanning-tree mst 1 priority 24576
spanning-tree mst 2 priority 28672
```

Use different switches as roots for different instances to balance paths.

## Troubleshooting

If switches do not appear to share the expected MST region:

```cisco
show spanning-tree mst configuration
```

Compare:

1. Name
2. Revision
3. VLAN mappings

Also check trunks:

```cisco
show interfaces trunk
```

A VLAN that is not carried across a trunk cannot behave as expected.

## CML lab

Build:

```text
        SW1
       /   \
     SW2---SW3
```

Map VLANs 10-20 to MST 1 and VLANs 30-40 to MST 2.

Make SW1 root for MST 1 and SW2 root for MST 2.

Observe which links forward and which become alternate paths.
