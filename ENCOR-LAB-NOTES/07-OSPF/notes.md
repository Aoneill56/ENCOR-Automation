# OSPF

OSPF is a link-state routing protocol and a major ENCOR topic.

## Basic configuration

```cisco
router ospf 1
 router-id 1.1.1.1
 network 10.0.12.0 0.0.0.3 area 0
 network 10.0.1.0 0.0.0.255 area 0
```

Verify:

```cisco
show ip ospf neighbor
show ip ospf interface brief
show ip ospf
show ip route ospf
```

## Neighbour troubleshooting

If no neighbour forms:

1. Interface up/up?
2. Correct IP/subnet?
3. OSPF enabled?
4. Same area?
5. Hello/dead timers match?
6. Authentication match?
7. Network type match?
8. MTU compatible?
9. Is the interface passive?

Useful:

```cisco
show ip ospf neighbor
show ip ospf interface GigabitEthernet2
show ip protocols
```

## Passive interface

```cisco
router ospf 1
 passive-interface GigabitEthernet1
```

Useful for advertising a connected network without forming an OSPF adjacency on that interface.

## Lab

Build:

```text
R1 -------- R2 -------- R3
```

Use area 0 initially.

Verify adjacency, routing-table entries and convergence after shutting down a link.
