"""
    PyIs Module

    Developed by Amirhossein Mohammadi
    Github: github.com/BlackIQ/pyis

    Last Update: Aug 9 2021
    Version: 1.9.3
"""

# Importing required libraries
from requests import get

version = "1.9.3"


class validations:
    """
        Validations Class
        Here we have classes for validate variables
    """

    class type:
        """
            Validations.Type Class
            Here are functions for check type of variables
        """

        @staticmethod
        def is_int(var):
            # Validations.Type.Is_int function
            # To check variable is int or not
            if type(var) == int:
                return True
            else:
                return False

        @staticmethod
        def is_string(var):
            # Validations.Type.Is_String function
            # To check variable is string or not
            if type(var) == str:
                return True
            else:
                return False

        @staticmethod
        def is_float(var):
            # Validations.Type.Is_Float function
            # To check variable is float or not
            if type(var) == float:
                return True
            else:
                return False

        @staticmethod
        def is_list(var):
            # Validations.Type.Is_List function
            # To check variable is list or not
            if type(var) == list:
                return True
            else:
                return False

        @staticmethod
        def is_bool(var):
            # Validations.Type.Is_Bool function
            # To check variable is bool or not
            if type(var) == bool:
                return True
            else:
                return False

        @staticmethod
        def is_dict(var):
            # Validations.Type.Is_Dict function
            # To check variable is dict or not
            if type(var) == dict:
                return True
            else:
                return False

        @staticmethod
        def is_tuple(var):
            # Validations.Type.Is_Tuple function
            # To check variable is tuple or not
            if type(var) == tuple:
                return True
            else:
                return False

        @staticmethod
        def is_function(var):
            # Validations.Type.Is_Function function
            # To check variable is function or not
            if callable(var):
                return True
            else:
                return False

    class amount:
        """
            Validations.Amount Class
            Here are functions for check amount of variables
        """

        @staticmethod
        def is_set(var):
            # Validations.Amount.Is_Set function
            # To check variable is swt or not
            if var != None:
                return True
            else:
                return False

        @staticmethod
        def is_empty(var):
            # Validations.Amount.Is_Empty function
            # To check variable is empty or not
            if var == None:
                return True
            else:
                return False

    class numbers:
        """
            Validations.Numbers Class
            Here are functions for check number is more or less or equal to zero
        """

        @staticmethod
        def is_positive(var):
            # Validations.Numbers.Is_Positive function
            # To check variable is positive or not
            if var > 0:
                return True
            else:
                return False

        @staticmethod
        def is_negative(var):
            # Validations.Numbers.Is_Negative function
            # To check variable is negative or not
            if var < 0:
                return True
            else:
                return False

        @staticmethod
        def is_zero(var):
            # Validations.Numbers.Is_Zero function
            # To check variable is zero or not
            if var == 0:
                return True
            else:
                return False


class internet:
    """
        Internet Class
        Here we have classes for internet checking
    """

    class check:
        """
            Internet.Check Class
            Here are functions for check status of urls
        """

        @staticmethod
        def is_up(url):
            # internet.Check.Is_Up function
            # To check url returns 200 or not
            if get(url).status_code == 200:
                return True

        @staticmethod
        def is_down(url):
            # internet.Check.Is_Down function
            # To check url not returns 200
            if get(url).status_code != 200:
                return True

    class errors:
        """
            Internet.Errors Class
            Here are functions for check client or server errors of urls
        """

        @staticmethod
        def is_forbidden(url):
            # internet.Errors.Is_Forbidden function
            # This function checks url forbidden or not
            if get(url).status_code == 403:
                return True

        @staticmethod
        def is_not_found(url):
            # internet.Errors.Is_Not_Found function
            # This function checks url not found or not
            if get(url).status_code == 404:
                return True

        @staticmethod
        def is_internal_server_error(url):
            # internet.Errors.Is_Internal_Server_Error function
            # This function checks url is 500 Error
            if get(url).status_code == 500:
                return True

    class cloudflare:
        """
            Internet.Cluoudflare Class
            Here are functions for check cloudflare errors
        """

        @staticmethod
        def is_web_down(url):
            # internet.Cloadflare.Is_Down function
            # This function check host that cloudflare routes it is down or not
            if get(url).status_code == 521:
                return True

        @staticmethod
        def is_ssl_failed(url):
            # internet.Cloadflare.Is_SSL_Failed function
            # This function check SSL of host
            if get(url).status_code == 525:
                return True

        @staticmethod
        def is_ssl_invalid(url):
            # internet.Cloadflare.Is_SSL_Invalid function
            # This function check SSL of host is valid or invalid
            if get(url).status_code == 526:
                return True

        @staticmethod
        def is_origin_unreachable(url):
            # internet.Cloadflare.Is_Origin_Unreachable function
            # This function check host is reachable or not
            if get(url).status_code == 523:
                return True
