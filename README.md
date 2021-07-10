## pyis

**pyis** is a library to check values in your python projects.

Check these out

- Installation
- Documentation

### Installation

- Way number 1 : **Using pip**

```
pip3 install pyis
```

- Way number 2 : **Clone and install**

```
git clone https://github.com/BlackIQ/pyis && cd pyis
pip3 install -e .
```

### Documentation

**pyis** has lots of functions that we will name them and say an aexample for each of them.

- `is_set()` is a function that check variable is set or not.

```python
i = "Hello"
ii = None

is_set(i) # Returns True
is_set(ii) # Returns False
```

- `is_empty()` is a function that check variable is empty or not.

```python
e = "Hey"
ee = None

is_empty(e) # Returns False
is_empty(ee) # Returns True
```

- `is_number()` is a function that check variable is **int** or not.

```python
v1 = 18
v2 = "string"

is_number(v1) # Returns True
is_number(v2) # Returns False
```

- `is_string()` is a function that check variable is **str** or not.

```python
v1 = "Annahita"
v2 = 3.14

is_string(v1) # Returns True
is_string(v2) # Returns False
```

- `is_float()` is a function that check variable is **float** or not.

```python
v1 = 3.14
v2 = ['hi', 'hey', 'hello']

is_float(v1) # Returns True
is_float(v2) # Returns False
```

- `is_list()` is a function that check variable is **list** or not.

```python
v1 = ['github', 'gitlab']
v2 = 2021

is_list(v1) # Returns True
is_list(v2) # Returns False
```

- `is_bool()` is a function that check variable is **bool** or not.

```python
v1 = True
v2 = "false"

is_bool(v1) # Returns True
is_bool(v2) # Returns False
```

- `is_positive()` is a function that check variable is **positive** or not.

```python
v1 = 20
v2 = 5 - 7

is_positive(v1) # Returns True
is_positive(v2) # Returns False
```

- `is_negative()` is a function that check variable is **negative** or not.

```python
v1 = 10 - 30
v2 = 1

is_negative(v1) # Returns True
is_negative(v2) # Returns False
```

- `is_zero()` is a function that check variable is **zero** or not.

```python
v1 = 0
v2 = 1

is_zero(v1) # Returns True
is_zero(v2) # Returns False
```

- `is_function()` is a function that check variable is **function** or not.

```python
def hello(name):
	print(f"Hello {name}")

is_function(hello) # Returns True
```
