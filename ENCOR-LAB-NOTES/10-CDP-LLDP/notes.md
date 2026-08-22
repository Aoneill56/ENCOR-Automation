# CDP and LLDP

CDP and LLDP provide neighbour discovery information.

## CDP

Verify:

```cisco
show cdp neighbors
show cdp neighbors detail
```

CDP can reveal:

- Device ID
- Local interface
- Hold time
- Capability
- Platform
- Remote port

## LLDP

Verify:

```cisco
show lldp neighbors
show lldp neighbors detail
```

Enable if required:

```cisco
lldp run
```

## Troubleshooting

If a neighbour is missing:

1. Is the interface up?
2. Is the protocol enabled?
3. Is discovery disabled on the interface?
4. Is the peer running the corresponding protocol?

These protocols are particularly useful in CML for confirming which interface connects to which device.
