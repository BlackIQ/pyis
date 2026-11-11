# pyis

Tiny helpers for common value checks in Python.

Instead of writing the same `isinstance` / `is None` / comparison conditions everywhere, call small named helpers.

```python
from pyis import validations

validations.type.is_string("hello")   # True
validations.amount.is_set(None)       # False
validations.numbers.is_positive(3)    # True
```

|        |                                                         |
| ------ | ------------------------------------------------------- |
| PyPI   | [pypi.org/project/pyis](https://pypi.org/project/pyis/) |
| Source | [GitHub](https://github.com/BlackIQ/pyis)               |

## Next

- [Install](learn/install.md)
- [Usage](learn/usage.md)
