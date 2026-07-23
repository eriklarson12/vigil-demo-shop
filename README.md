# vigil-demo-shop

A small e-commerce system used as the subject of Vigil's incident demos.
Every commit here is planted: the history reproduces the scenarios in
`simulator/scenarios/` so Vigil's deterministic scorer has a real repo to rank.

| Service | Tier | Path |
|---|---|---|
| checkout | 0 | `services/checkout/` |
| auth | 0 | `services/auth/` |
| payments-db | 0 | `db/` |
| orders | 1 | `services/orders/` |
| inventory | 1 | `services/inventory/` |

Not a real shop. Do not deploy it.
