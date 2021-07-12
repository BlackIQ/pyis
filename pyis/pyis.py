repeted = []

version = "0.11.2"


def is_set(var):
    if var != None:
        return True
    else:
        return False


def is_empty(var):
    if var == None:
        return True
    else:
        return False


def is_number(var):
    if type(var) == int:
        return True
    else:
        return False


def is_string(var):
    if type(var) == str:
        return True
    else:
        return False


def is_float(var):
    if type(var) == float:
        return True
    else:
        return False


def is_list(var):
    if type(var) == list:
        return True
    else:
        return False


def is_bool(var):
    if type(var) == bool:
        return True
    else:
        return False


def is_dict(var):
    if type(var) == dict:
        return True
    else:
        return False


def is_tuple(var):
    if type(var) == tuple:
        return True
    else:
        return False


def is_positive(var):
    if var > 0:
        return True
    else:
        return False


def is_negative(var):
    if var < 0:
        return True
    else:
        return False


def is_zero(var):
    if var == 0:
        return True
    else:
        return False


def is_function(var):
    if callable(var):
        return True
    else:
        return False


def item_repeted(lst):
    for item in lst:
        if item in repeted:
            pass
        else:
            repeted.append(item)
    return repeted
