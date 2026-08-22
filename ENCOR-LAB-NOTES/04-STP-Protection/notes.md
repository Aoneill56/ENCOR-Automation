# STP Protection

## BPDU Guard

Used on edge/access ports:

```cisco
interface Ethernet0/10
 spanning-tree portfast
 spanning-tree bpduguard enable
```

Verify err-disabled ports:

```cisco
show interfaces status err-disabled
show logging
```

## Root Guard

Prevents an unexpected switch from becoming root through a protected interface:

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

## Troubleshooting

```cisco
show spanning-tree summary
show spanning-tree interface Ethernet0/1 detail
show interfaces status err-disabled
show errdisable recovery
show logging
```

Always identify the cause before simply recovering an err-disabled port.
