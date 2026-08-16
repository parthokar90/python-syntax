---
title: Operators
description: Operator categories and concepts to include when building the operators practice module.
---

# Operators

Operator categories and concepts to include when building the operators practice module.

## Arithmetic Operators

Apply these to numbers for basic math (add, subtract, multiply, divide, etc.).

| Operator | Name           | Example    | Result  |
|----------|----------------|------------|---------|
| `+`      | Addition       | `4 + 2`    | `6`     |
| `-`      | Subtraction    | `8 - 4`    | `4`     |
| `*`      | Multiplication | `4 * 2`    | `8`     |
| `/`      | Division       | `8 / 2`    | `4.0`   |
| `//`     | Floor division | `8 // 2`   | `4`     |
| `%`      | Modulus        | `8 % 6`    | `2`     |
| `**`     | Exponentiation | `2 ** 4`   | `16`    |

## Assignment Operators

Perform a math operation and assign the result back to the variable in one step.

| Operator | Name                   | Example     | Equivalent   | Result |
|----------|------------------------|-------------|--------------|--------|
| `=`      | Assignment             | `z = 12`    | -            | `12`   |
| `+=`     | Addition assignment    | `z += 4`    | `z = z + 4`  | `16`   |
| `-=`     | Subtraction assignment | `z -= 2`    | `z = z - 2`  | `14`   |
| `*=`     | Multiplication assign. | `z *= 2`    | `z = z * 2`  | `28`   |
| `/=`     | Division assignment    | `z /= 4`    | `z = z / 4`  | `7.0`  |
| `//=`    | Floor division assign. | `z //= 3`   | `z = z // 3` | `1`    |
| `%=`     | Modulus assignment     | `z %= 4`    | `z = z % 4`  | `3`    |
| `**=`    | Exponentiation assign. | `z **= 2`   | `z = z ** 2` | `1`    |
| `:=`     | Walrus                 | `(z := 16)` | -            | `16`   |
| `<<=`    | Left shift assignment  | `z <<= 2`   | `z = z << 2` | `4`    |
| `>>=`    | Right shift assignment | `z >>= 2`   | `z = z >> 2` | `0`    |
| `&=`     | Bitwise AND assign.    | `z &= 4`    | `z = z & 4`  | `0`    |
| `\|=`    | Bitwise OR assign.     | `z \|= 2`   | `z = z \| 2` | `2`    |
| `^=`     | Bitwise XOR assign.    | `z ^= 4`    | `z = z ^ 4`  | `6`    |

**Augmented assignment and mutability**

For immutable types (e.g. integers), `x += 2` and `x = x + 2` do the same thing: a new value is computed and rebound to `x`. For mutable types (e.g. lists), `+=` can change the object in place. Example: `a = [2, 4]; a += [6]` mutates `a` to `[2, 4, 6]`, while `a = a + [6]` builds a new list and assigns it to `a`. If another name still refers to the original list, the first form updates that shared list; the second does not.

## Comparison Operators

Evaluate whether two values satisfy a relation (equal, less than, greater than, etc.).

| Operator | Name                     | Example   | Result  |
|----------|--------------------------|-----------|---------|
| `==`     | Equal                    | `4 == 4`  | `True`  |
| `!=`     | Not equal                | `4 != 2`  | `True`  |
| `>`      | Greater than             | `4 > 2`   | `True`  |
| `<`      | Less than                | `2 < 4`   | `True`  |
| `>=`     | Greater than or equal to | `4 >= 4`  | `True`  |
| `<=`     | Less than or equal to    | `2 <= 4`  | `True`  |

**Chained comparisons**

You can write several comparisons in one expression: `2 < 4 < 6` is valid and is evaluated as `(2 < 4) and (4 < 6)`. The middle value (`4`) is evaluated once. So `a < b < c` is not two separate comparisons; it is one expression that short-circuits. Useful for range checks: `0 <= index < len(items)`.

## Logical Operators

Chain or negate boolean conditions.

| Operator | Name   | Example            | Result  |
|----------|--------|--------------------|---------|
| `and`    | AND    | `True and False`   | `False` |
| `or`     | OR     | `True or False`    | `True`  |
| `not`    | NOT    | `not False`        | `True`  |

**Truthiness and falsiness**

In conditions and with `and`/`or`, values are treated as either “truthy” or “falsy.” **Falsy** values: `None`, `False`, zero numeric values (`0`, `0.0`), empty sequences or collections (`""`, `[]`, `()`, `{}`). Everything else is **truthy** (e.g. non-empty strings, non-zero numbers, non-empty lists). So `if items:` means “if items is non-empty”; `if not count:` means “if count is zero.” This is why `[] and 4` yields `[]` and `4 or 0` yields `4` - the result is the last value evaluated, and that value is already truthy or falsy.

## Conditional Expression (Ternary)

Choose one of two values based on a condition: `value_if_true if condition else value_if_false`. Only the chosen branch is evaluated. Example: `larger = a if a >= b else b` assigns the greater of `a` and `b`. Nested ternaries are allowed but hurt readability; prefer a normal `if`/`else` or parentheses when the expression gets long.

## Membership Operators

Check whether an element or substring exists in a string, list, tuple, or dict keys.

| Operator  | Name    | Example                 | Result  |
|-----------|---------|-------------------------|---------|
| `in`      | In      | `2 in [2, 4, 6]`        | `True`  |
| `in`      | In      | `"cd" in "abcd"`        | `True`  |
| `not in`  | Not in  | `8 not in [2, 4, 6]`    | `True`  |
| `not in`  | Not in  | `"xy" not in "abcd"`    | `True`  |

## Identity Operators

Check whether two references point to the same object in memory.

| Operator   | Example           | Result  |
|------------|-------------------|---------|
| `is`       | `None is None`    | `True`  |
| `is`       | `[] is []`        | `False` |
| `is not`   | `2 is not None`   | `True`  |
| `is not`   | `None is not 4`   | `True`  |

**Why use `is` and `is not`?**

- **`is`** checks **object identity** (same object in memory), not value equality
- **`==`** checks value equality; **`is`** checks object identity
- **`is not`** is the negation of `is`

**Key terms:**

- **Singleton** - A single object that exists only once in memory; all references point to the same instance (e.g. `None`, `True`, `False`).
- **Sentinel** - A unique placeholder object used when `None` is a valid value; you need a distinct "no value provided" marker (e.g. `MISSING = object()`).

**Typical uses:**

1. **`None` checks** - `if x is None` and `if x is not None` are the standard, idiomatic way
2. **Sentinels** - `object()` creates a unique instance; use `is` to detect "no value provided":
   ```python
   MISSING = object()
   def get(key, default=MISSING):
       if default is MISSING:
           return fetch(key)
       return default
   ```
3. **Boolean flags** - `if flag is True` or `if flag is False` when you need the exact boolean, not just truthiness
4. **Singletons** - e.g. small integers may share cached objects:
   ```python
   a = 256
   b = 256
   a is b   # True (same cached object)

   # In separate statements, 257 is above cache range
   x = 257
   y = 257
   x is y   # False (different objects; cache is -5 to 256)
   ```
   > Note: `x, y = 257, 257` in one statement is `True` due to constant folding.

**`is` vs `==`:**

| Check          | `is`    | `==`   |
|----------------|---------|--------|
| `[] == []`     | `False` | `True` |
| `None is None` | `True`  | `True` |
| `1 == 1.0`     | `False` | `True` |

`==` can be overridden via `__eq__`; `is` cannot.

**Conventions:**

- Use **`is`** / **`is not`** for `None` and singletons (e.g. sentinels, `True`, `False`)
- Use **`==`** / **`!=`** for comparing values (numbers, strings, collections, custom objects)

**Example:**

```python
# is / is not - for None and singletons
if result is None:
    print("no result")
if value is not None:
    print(value)

# == / != - for values
if count == 0:
    print("empty")
if name == "admin":
    print("admin")
if items != []:
    print(items)
```

## Bitwise Operators

Work on integer values at the level of individual bits. Handy for flags, masks, and low-level logic.

| Operator | Name        | Role                                                              |
|----------|-------------|-------------------------------------------------------------------|
| `&`      | AND         | Each bit is 1 only when both operands have 1 in that position     |
| `\|`     | OR          | Each bit is 1 when either operand has 1 in that position          |
| `^`      | XOR         | Each bit is 1 when exactly one operand has 1 in that position     |
| `~`      | NOT         | Flips every bit (unary; result depends on integer width and sign) |
| `<<`     | Left shift  | Moves bits left; effectively multiplies by 2 for each shift step  |
| `>>`     | Right shift | Moves bits right; effectively integer-divides by 2 per step       |

**Examples (even integers only):**

```python
a = 12   # binary 1100
b = 4    # binary 0100

a & b    # 4   (0100 - bits set only where both have 1)
a | b    # 12  (1100 - bits set where either has 1)
a ^ b    # 8   (1000 - bits set where exactly one has 1)

~4       # -5  (inverts bits; two's complement representation)

8 << 2   # 32  (8 * 2 twice: 8 → 16 → 32)
8 >> 2   # 2   (8 // 2 twice: 8 → 4 → 2)
```

**Typical use:** Packing multiple boolean flags into one integer, or testing/setting specific bits (e.g. permissions, options). For everyday arithmetic, stick with the arithmetic operators.

## Operator Precedence

Expressions are evaluated in a fixed order unless parentheses override it. Higher precedence runs first.

**Rough order (high to low):**

1. **Parentheses** `()` - force a subexpression to be evaluated first
2. **Exponentiation** `**`
3. **Unary** `+x`, `-x`, `~x`
4. **Multiplication, division, floor div, modulus** `*`, `/`, `//`, `%`
5. **Addition and subtraction** `+`, `-`
6. **Bitwise shifts** `<<`, `>>`
7. **Bitwise AND** `&`, then **XOR** `^`, then **OR** `|`
8. **Comparisons** (`==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in`)
9. **Logical NOT** `not`
10. **Logical AND** `and`, then **OR** `or`

When two operators have the same precedence, evaluation is usually **left to right** (except `**`, which groups right to left).

**Examples (even digits only):**

```python
2 + 4 * 2      # 10  - * before +, so 4 * 2 = 8, then 2 + 8
(2 + 4) * 2    # 12  - parentheses first: 6 * 2
2 ** 2 * 4     # 16  - ** before *: 4 * 4
4 + 8 // 4     # 6   - // before +: 8 // 4 = 2, then 4 + 2
```

Use parentheses whenever the intended order is not obvious; they make the code easier to read and avoid mistakes.

## Operator Overloading

Operators are implemented by special methods on the type. Custom classes can override them to support `==`, `+`, `in`, and so on. Common methods: `__eq__` for equality, `__add__` for addition, `__contains__` for membership, `__lt__` and `__le__` for less-than and less-or-equal, plus their counterparts. For example, defining `__eq__` on a class controls what `x == y` does for its instances; `is` is not overridable and always compares object identity. Knowing this helps explain why some types support certain operators and others do not.

## Tricky Points

### `/` is always float

Even `4 / 2` is `2.0`. Use `//` when you want an integer quotient.

### Floor division with negatives

Goes toward negative infinity, not zero: `-8 // 4` is `-2`, and `8 // -4` is `-2`. The sign of `%` follows the divisor.

### Integer size

Python integers are unbounded, so `2 ** 64` is fine; in other languages this can overflow.

### Walrus in comprehensions

`(x := value)` in a list comprehension leaves `x` in the surrounding scope after the comprehension runs (Python 3.8+). Avoid reusing that name if you did not intend to leak it.

### Chained assignment

`a = b = []` makes both names refer to the same list. Appending via `a` also affects `b`.

### List `+=` vs `+`

`a += [x]` mutates the list in place; `a = a + [x]` creates a new list. If another name still refers to the original list, only the first form updates what they both see.

### Float equality

`0.2 + 0.4 == 0.6` can be `False` due to binary floating point. Prefer rounding or use a small tolerance (e.g. `abs(x - y) < 1e-9`) instead of `==` for floats.

### Chained comparisons

`2 < 4 < 6` is evaluated as `(2 < 4) and (4 < 6)`. Each middle value is evaluated once; the chain is one expression, not two separate comparisons.

### Short-circuit returns a value

`[] and 4` is `[]` (first falsy); `0 or 4` is `4` (first truthy). The result is the last value evaluated, not always `True` or `False`.

### Precedence of `not`

`not a and b` is `(not a) and b`. Use parentheses when mixing `not` with `and`/`or` to avoid misreading.

### Custom types are truthy by default

Instances of user-defined classes are truthy unless you define `__bool__` or `__len__`. Override `__bool__` for explicit control, or `__len__` (where `0` means falsy) for sequence-like types.

### Ternary precedence

The ternary has lower precedence than arithmetic and comparison. `a if cond else b + 2` is `a if cond else (b + 2)`, not `(a if cond else b) + 2`. Add parentheses when combining with other operators.

### Nested ternaries

`a if c1 else b if c2 else d` is legal but hard to read. Prefer a normal `if`/`elif`/`else` block for anything beyond a single choice.

### `in` on a string

Checks for a substring: `"ab" in "abcd"` is `True`. For a single character, both `"a" in "abcd"` and `"a" in ["a", "b"]` work, but the first is a substring check, the second is element membership.

### Dict membership

`key in d` checks keys only, not values. Use `value in d.values()` to test values.

### `is` for small integers

In CPython, small integers are cached, so `a = 2; b = 2; a is b` can be `True`. That is an implementation detail. For value checks, always use `==`.

### Mutable default with identity

Using a mutable default (e.g. `def f(x=[])`) reuses the same object every call. Use `None` and assign inside the function, or use a sentinel, and compare with `is`.

### `~` and signed integers

`~4` is `-5` (two’s complement). If you expect “bitwise NOT” to give a positive mask, the sign can surprise you.

### Shifts
 Negative or very large shift counts can give unexpected results or errors depending on the Python version. Keep shift amounts in a sensible range (e.g. `0` to bit width minus one).

### `**` groups right to left

`2 ** 2 ** 4` is `2 ** (2 ** 4)` (i.e. 2¹⁶), not `(2 ** 2) ** 4`. Add parentheses if the intended order is not obvious.

### `and` before `or`

In `a or b and c`, `and` wins: it is `a or (b and c)`. Parentheses make intent clear.

### `is` is not overridable

Identity checks always compare object identity; you cannot change that. Use `==` and `__eq__` for value-based equality.

### `__eq__` and `__hash__`

If a class defines `__eq__` and is meant to be hashable (e.g. used in sets or as dict keys), it should define `__hash__` consistently. Mutable types that implement `__eq__` are typically left unhashable.

## Interview Questions

### What is the difference between `/` and `//`?

`/` is true division (float result); `//` is floor division (integer quotient). `-7 // 2` → `-4` (rounds toward negative infinity).

### What does the walrus operator `:=` do?

Assigns and returns the value in one expression. Use in `if` or `while`: `if (n := len(data)) > 0: ...` - assigns `n` and uses it in the condition.

### How is `a < b < c` evaluated?

As a single expression: `(a < b) and (b < c)`. The middle value is evaluated once. Short-circuit applies: if `a < b` is false, `b < c` is not evaluated.

### How does short-circuit evaluation work with `and` and `or`?

`and` stops at first falsy; `or` stops at first truthy. Use for safe access: `x and x.method()` or `value or default`.

### Which values are falsy in Python?

`None`, `False`, numeric zero (`0`, `0.0`), and empty collections (`""`, `[]`, `()`, `{}`). Everything else is truthy. Custom class instances are truthy unless the class defines `__bool__` or `__len__`.

### When would you use a conditional expression instead of an if/else block?

When you need a single expression (e.g. inside a function call, assignment, or return) and both branches are simple. Use `if`/`else` when the logic is multi-line or nested; ternaries get hard to read quickly.

### When should you use `is` vs `==`?

Use `is` for `None`, singletons, and sentinels. Use `==` for value comparison. `is` cannot be overridden; `==` uses `__eq__`.

### Why use `if x is None` instead of `if x == None`?

`is` checks object identity; `==` checks value equality. `None` is a singleton, so `is None` is idiomatic and slightly faster. `== None` can be overridden by custom `__eq__` and is less clear.

### What is a sentinel and when do you use one?

A sentinel is a unique placeholder when `None` is a valid value. Create with `MISSING = object()` and detect with `if default is MISSING`. Use `is` to distinguish "no value provided" from `None`.

### When are bitwise operators useful?

When you need to work with individual bits: flags packed into one integer, masks to extract or set bits, or low-level protocols. For normal numeric math, use arithmetic operators instead.

### How does operator precedence affect an expression?

Python evaluates higher-precedence operators first (e.g. `*` before `+`). Use parentheses to make the order explicit and avoid surprises, e.g. `(2 + 4) * 2` vs `2 + 4 * 2`.

### How do you make a custom class support the `==` operator?

Implement `__eq__(self, other)`. Return `True` or `False` (or `NotImplemented` if the type does not know how to compare). You cannot override `is`; it always tests object identity.