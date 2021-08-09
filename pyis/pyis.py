"""
    PyIs Module
    Developed by Amirhossein Mohammadi
    Github: github.com/BlackIQ/pyis
"""

version = "0.15.2"


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
            if var != None:
                return True
            else:
                return False

        @staticmethod
        def is_empty(var):
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
            if var > 0:
                return True
            else:
                return False

        @staticmethod
        def is_negative(var):
            if var < 0:
                return True
            else:
                return False

        @staticmethod
        def is_zero(var):
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
            return url

        @staticmethod
        def is_down(url):
            return url

    class errors:
        """
            Internet.Errors Class
            Here are functions for check client or server errors of urls
        """
        @staticmethod
        def is_forbidden(url):
            return url

        @staticmethod
        def is_not_found(url):
            return url

        @staticmethod
        def is_bad_request(url):
            return url

        @staticmethod
        def is_Unauthorized(url):
            return url

        @staticmethod
        def is_method_not_allowed(url):
            return url

        @staticmethod
        def is_bad_gateway(url):
            return url

        @staticmethod
        def is_internal_server_error(url):
            return url

    class cloudflare:
        """
            Internet.Cluoudflare Class
            Here are functions for check cloudflare errors
        """
        @staticmethod
        def is_web_down(url):
            return url

        @staticmethod
        def is_timeout(url):
            return url

        @staticmethod
        def is_ssl_failed(url):
            return url

        @staticmethod
        def is_ssl_invalid(url):
            return url

        @staticmethod
        def is_origin_unreachable(url):
            return url