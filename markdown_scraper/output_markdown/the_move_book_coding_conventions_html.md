# The Move Book

## Naming

```bash
module book::conventions { /* ... */ }
module book::common_practices { /* ... */ }
```

```bash
const MAX_PRICE: u64 = 1000;
const EInvalidInput: u64 = 0;
```

```bash
public fun add(a: u64, b: u64): u64 { a + b }
public fun create_if_not_exists() { /* ... */ }
```

```bash
public struct Hero has key {
    id: UID
    value: u64,
    another_value: u64,
}

public struct AdminCap has key { id: UID }
```

```bash
public fun value(h: &Hero): u64 { h.value }

public use fun hero_health as Hero.health;
public fun hero_health(h: &Hero): u64 { h.another_value }

public use fun boar_health as Boar.health;
public fun boar_health(b: &Boar): u64 { b.another_value }
```