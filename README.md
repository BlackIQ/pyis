## pyis

**pyis** is a library to check values in your python projects.

- Installation
- Documentation
- Examples
- Developers
- Next Update

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

First import it.

```python
from pyis import *
```

- `version` for check version

```python
print(version)
```

- `is_set()` is a function that check variable is set or not.

```python
i = "Hello"
ii = None

is_set(i)  # Returns True
is_set(ii)  # Returns False
```

- `is_empty()` is a function that check variable is empty or not.

```python
e = "Hey"
ee = None

is_empty(e)  # Returns False
is_empty(ee)  # Returns True
```

- `is_number()` is a function that check variable is **int** or not.

```python
v1 = 18
v2 = "string"

is_number(v1)  # Returns True
is_number(v2)  # Returns False
```

- `is_string()` is a function that check variable is **str** or not.

```python
v1 = "Annahita"
v2 = 3.14

is_string(v1)  # Returns True
is_string(v2)  # Returns False
```

- `is_float()` is a function that check variable is **float** or not.

```python
v1 = 3.14
v2 = ['hi', 'hey', 'hello']

is_float(v1)  # Returns True
is_float(v2)  # Returns False
```

- `is_list()` is a function that check variable is **list** or not.

```python
v1 = ['github', 'gitlab']
v2 = 2021

is_list(v1)  # Returns True
is_list(v2)  # Returns False
```

- `is_bool()` is a function that check variable is **bool** or not.

```python
v1 = True
v2 = "false"

is_bool(v1)  # Returns True
is_bool(v2)  # Returns False
```

- `is_positive()` is a function that check variable is **positive** or not.

```python
v1 = 20
v2 = 5 - 7

is_positive(v1)  # Returns True
is_positive(v2)  # Returns False
```

- `is_negative()` is a function that check variable is **negative** or not.

```python
v1 = 10 - 30
v2 = 1

is_negative(v1)  # Returns True
is_negative(v2)  # Returns False
```

- `is_zero()` is a function that check variable is **zero** or not.

```python
v1 = 0
v2 = 1

is_zero(v1)  # Returns True
is_zero(v2)  # Returns False
```

- `is_function()` is a function that check variable is **function** or not.

```python
def hello(name):
    print(f"Hello {name}")


is_function(hello)  # Returns True
```

### Examples

Here are some examples that you can get the point better.

**Numbers, check number is float or int. Then check is positive or negative or zero**

Here we use `is_number` to check if input is `int` and `is_float` to see input is `float`.

then we use functions for check value. As you know, we have:

- `is_positive` for check if number is more than 0.
- `is_negative` for check if number is less than 0.
- `is_zero` for check if number is exactly 0.

```python
number = input("Give me number")

# Check number is int or not
if is_number(number):
    # Number is more than 0 function
    if is_positive(number):
        print("Number is positive")
    # Number is less than 0 function
    elif is_negative(number):
        print("Number is negative")
    # Number is equal to 0 function
    elif is_zero(number):
        print("Number is zero")
# Check number is float or not
elif is_float(number):
    # Number is more than 0 function
    if is_positive(number):
        print("Number is positive")
    # Number is less than 0 function
    elif is_negative(number):
        print("Number is negative")
    # Number is equal to 0 function
    elif is_zero(number):
        print("Number is zero")
```

**Set or empty and talking about `tuple`, `list` and `dictionary`**

Think there is a `list` or `dictionary` that you want to check values.

For check if var is:

- `list` we use `is_list`.
- `tuple` we use `is_tuple`.
- `dict` we use `is_dict`.

So we use `is_set` to check if var is set or not. For check is var is empty we use `is_empty`.

```python
tpl = (1, 2, 5)
l = ['Hi', 10]
dct = {'name': None}

# Function returns ( True ). Parm is dictionary
if is_dict(dct):
    # Here is a tuple.
    if is_tuple(tpl):
        print("This is a tuple")
    # Lets check list
    if is_list(l):
        # See is it set or not. Returns ( True )
        if is_set(l[1]):
            print("This item is set")
    # Here we get ( True ). Parm is not set. It is empty
    if is_empty(dct['name']):
        print("This var is empty")
```

**Strings and Booleans**

Time of say some examples for strings and booleans.

When there is something and you want to check is it `string` you can use `is_string`. We do same for `bool`, `is_bool`
for see var is `boolean` or not.

So we know this two functions now:

- `is_string` for check strings.
- `is_bool` to see var is `boolean`

```python
lst = ['False', 'amir', True]

# Here it will returns ( True ). Why? Item is string
if is_string(lst[0]):
    print("Item 1 is string")

# Now we get ( False ). As you can see, item is string
if is_bool(lst[1]):
    print("This item is boolean")

# Nice ( True ). Item is boolean
if is_bool(lst[2]):
    print("I can see a boolean")
```

**Functions checking**

See, think there is `callable` var. How do you check? You can use `is_function` to check it.

So, how user can check functions?

- `is_function` for check function

```python
def you(name, friend):
    print(f"Hello {name} and {friend}!")


# Get True or False. You is a function, so it returns ( True )
if is_function(you):
    print("Look, a function!")
```

### Developers

Amirhossein Mohammadi.

Pull Requests are welcome to every one.

### Next Update

- [ ] Add most repeted item in a list
- [ ] Add class checker
- [ ] Add link string checker
- [ ] Add IP checker
- [x] Add version value

**pyis** 2021 &copy;
