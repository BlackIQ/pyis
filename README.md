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

- `python is_set()` is a function that check variable is set or not.

```python
i = "Hello"
ii = None

is_set(i) # Returns True
is_set(ii) # Returns False
