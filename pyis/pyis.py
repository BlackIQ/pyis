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
		
def is_function(var):
	if callable(var):
		return True
	else:
		return False