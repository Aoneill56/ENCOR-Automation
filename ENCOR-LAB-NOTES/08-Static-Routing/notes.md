# Static Routing

Static routes are manually configured paths.

## Configuration

```cisco
ip route 10.0.23.0 255.255.255.252 10.0.12.2
```

Or specify an exit interface where appropriate:

```cisco
ip route 10.0.23.0 255.255.255.252 GigabitEthernet2
```

## Verify

```cisco
show ip route
show ip route 10.0.23.0
```

Test:

```cisco
ping 10.0.23.1
traceroute 10.0.23.1
```

## Troubleshooting

Ask:

1. Is the next hop reachable?
2. Does the route appear in the routing table?
3. Is the destination prefix correct?
4. Is there a return route?
5. Is ARP resolving where necessary?

Useful:

```cisco
show ip route
show arp
ping <next-hop>
ping <destination>
traceroute <destination>
```
