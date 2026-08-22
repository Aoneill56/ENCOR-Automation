# RSTP / Rapid PVST+

RSTP (802.1w) provides faster convergence. Cisco Rapid PVST+ runs a rapid spanning-tree instance per VLAN.

Legacy 802.1D STP is intentionally excluded.

## Port roles

- Root
- Designated
- Alternate
- Backup

## Port states

- Discarding
- Learning
- Forwarding

Do not confuse a port role with a port state.

## Configure Rapid PVST+

```cisco
spanning-tree mode rapid-pvst
```

Choose a root explicitly:

```cisco
spanning-tree vlan 10 priority 24576
```

or:

```cisco
spanning-tree vlan 10 root primary
```

Verify:

```cisco
show spanning-tree root
show spanning-tree vlan 10
show spanning-tree summary
```

## PortFast

For end-host ports:

```cisco
interface Ethernet0/10
 spanning-tree portfast
```

PortFast does not disable STP. Do not use it on switch-to-switch links.

## BPDU Guard

```cisco
interface Ethernet0/10
 spanning-tree portfast
 spanning-tree bpduguard enable
```

Troubleshoot:

```cisco
show interfaces status err-disabled
show logging
```

## Troubleshooting blocked ports

```cisco
show spanning-tree vlan 10
```

Ask:

1. Who is root?
2. What is this port's role?
3. What is the root path cost?
4. What is the peer's role?
5. Is the blocked path expected?

A blocked STP path may be correct behaviour preventing a Layer-2 loop.
