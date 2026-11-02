# Usage

Everything lives under `validations`:

```python
from pyis import validations
```

## Type checks — `validations.type`

Uses exact `type(x) is ...` (not `isinstance`), except `is_function` which uses `callable`.

| Method           | True when          |
| ---------------- | ------------------ |
| `is_int(x)`      | `type(x) is int`   |
| `is_string(x)`   | `type(x) is str`   |
| `is_float(x)`    | `type(x) is float` |
| `is_list(x)`     | `type(x) is list`  |
| `is_bool(x)`     | `type(x) is bool`  |
| `is_dict(x)`     | `type(x) is dict`  |
| `is_tuple(x)`    | `type(x) is tuple` |
| `is_function(x)` | `callable(x)`      |

```python
validations.type.is_int(1)          # True
validations.type.is_string("a")     # True
validations.type.is_list([1, 2])    # True
validations.type.is_function(print) # True
```

## Presence — `validations.amount`

| Method        | True when       |
| ------------- | --------------- |
| `is_set(x)`   | `x is not None` |
| `is_empty(x)` | `x is None`     |

```python
validations.amount.is_set(0)     # True
validations.amount.is_empty(None)  # True
```

## Numbers — `validations.numbers`

| Method           | True when |
| ---------------- | --------- |
| `is_positive(x)` | `x > 0`   |
| `is_negative(x)` | `x < 0`   |
| `is_zero(x)`     | `x == 0`  |

```python
validations.numbers.is_positive(2.5)  # True
validations.numbers.is_zero(0)        # True
```
