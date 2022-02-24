## Boolean Logic

## Initialised vs. Class comparison

*dirty-equals* allows comparison with types regardless of whether they've been initialised.

This saves users adding `()` in lots of places.

Example:

```py title="Initialised vs. Uninitialised"
from dirty_equals import IsInt

# these two cases are the same
assert 1 == IsInt
assert 1 == IsInt()
```

* pytest compatibility, including `__eq__` vs `__ne__`

```ansi-color
{! docs/test.ansi !}
```
