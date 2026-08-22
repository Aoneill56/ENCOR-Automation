# STP Protection

## BPDU Guard

Best suited to edge/access ports:

```cisco
interface Ethernet0/10
 spanning-tree portfast
 spanning-tree bpduguard enable
```

Check:

```cisco
show interfaces status err-disabled
show logging
```

## Root Guard

Prevents an unexpected switch from becoming the root through a protected interface:

```cisco
interface Ethernet0/1
 spanning-tree guard root
```

## Loop Guard

Helps protect against certain failures where BPDUs unexpectedly stop arriving:

```cisco
interface Ethernet0/1
 spanning-tree guard loop
```

## BPDU Filter

Suppresses BPDUs and must be used carefully because it can undermine STP protection.

## Useful verification

```cisco
show spanning-tree summary
show spanning-tree root
show spanning-tree interface Ethernet0/1 detail
show interfaces status err-disabled
show errdisable recovery
show logging
```

## Troubleshooting mental model

When a link blocks unexpectedly:

1. Who is root?
2. What is this port's role?
3. What is the path cost?
4. What is the peer's role?
5. Is the VLAN carried?
6. Is this STP behavior or a physical/link problem?
