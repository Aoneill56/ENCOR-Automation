# RSTP / Rapid PVST+

RSTP (802.1w) provides faster convergence than legacy STP. Cisco Rapid PVST+ runs a rapid spanning-tree instance per VLAN.

## Port roles

| Role | Purpose |
|---|---|
| Root | Best path toward the root bridge |
| Designated | Forwarding port for a segment |
| Alternate | Backup path toward the root |
| Backup | Backup for a designated port on the same switch/segment |

## Port states

RSTP uses:

- Discarding
- Learning
- Forwarding

Do not confuse a **port role** with a **port state**.

## Root bridge

The lowest bridge ID wins. Conceptually:

`Bridge ID = priority + system ID extension + MAC address`

For deterministic designs, explicitly choose the root.

```cisco
spanning-tree vlan 10 root primary
```

or:

```cisco
spanning-tree vlan 10 priority 24576
```

Verify:

```cisco
show spanning-tree root
show spanning-tree vlan 10
```

## Edge ports / PortFast

For end-host ports:

```cisco
interface Ethernet0/10
 spanning-tree portfast
```

PortFast does **not** disable STP. It makes an edge port transition to forwarding quickly.

Do not use PortFast on switch-to-switch links.

## BPDU Guard

```cisco
interface Ethernet0/10
 spanning-tree portfast
 spanning-tree bpduguard enable
```

If a BPDU is received, the port can be err-disabled.

Global defaults are also possible:

```cisco
spanning-tree portfast default
spanning-tree bpduguard default
```

## Study distinction

PortFast = edge behavior.

BPDU Guard = protects the edge-port assumption.
