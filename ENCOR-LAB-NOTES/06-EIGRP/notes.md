# EIGRP

EIGRP is a Cisco-developed advanced distance-vector routing protocol.

For ENCOR, focus on:

- Neighbour relationships
- Topology table
- Successor
- Feasible successor
- Feasible Distance
- Reported Distance
- Metrics
- Summarisation
- Troubleshooting

## Basic configuration

Classic:

```cisco
router eigrp 100
 network 10.0.0.0 0.0.0.255
 network 10.0.12.0 0.0.0.3
```

Named EIGRP:

```cisco
router eigrp CAMPUS
 address-family ipv4 unicast autonomous-system 100
  network 10.0.0.0 0.0.0.255
  network 10.0.12.0 0.0.0.3
  no shutdown
 exit-address-family
```

Verify:

```cisco
show ip eigrp neighbors
show ip eigrp topology
show ip route eigrp
show ip protocols
```

## Neighbour troubleshooting

If no neighbour forms:

1. Interface up/up?
2. Correct subnet?
3. EIGRP enabled?
4. Same AS?
5. Interface accidentally passive?
6. Authentication mismatch?
7. K-values compatible?
8. EIGRP packets filtered?

Useful:

```cisco
show ip eigrp neighbors
show ip eigrp interfaces
show ip protocols
```

## Successor and feasible successor

The successor is the current best path.

A feasible successor is a qualifying loop-free backup path.

The feasibility condition is:

```text
Reported Distance < Feasible Distance
```

View the topology:

```cisco
show ip eigrp topology
```

## Metric

Default EIGRP metric is primarily influenced by:

- Bandwidth
- Delay

Check:

```cisco
show interfaces GigabitEthernet1
show ip protocols
```

## Summarisation

Example:

```cisco
interface GigabitEthernet1
 ip summary-address eigrp 100 10.10.0.0 255.255.252.0
```

Verify:

```cisco
show ip route
show ip eigrp topology
```

## Lab

```text
R1 -------- R2 -------- R3
```

Use:

```text
10.0.12.0/30
10.0.23.0/30
```

Configure EIGRP AS 100.

Then:

1. Verify neighbours.
2. Verify EIGRP routes.
3. Shut down a link.
4. Observe topology and routing tables.
5. Restore it.
6. Add a second path.
7. Investigate feasible successors.
