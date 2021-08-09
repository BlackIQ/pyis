"""
    PyIs Module
    Developed by Amirhossein Mohammadi
    Github: github.com/BlackIQ/pyis
"""

version = "0.15.2"


class validations:
    class type:
        @staticmethod
        def is_int(var):
            if type(var) == int:
                return True
            else:
                return False

        @staticmethod
        def is_string(var):
            if type(var) == str:
                return True
            else:
                return False

        @staticmethod
        def is_float(var):
            if type(var) == float:
                return True
            else:
                return False

        @staticmethod
        def is_list(var):
            if type(var) == list:
                return True
            else:
                return False

        @staticmethod
        def is_bool(var):
            if type(var) == bool:
                return True
            else:
                return False

        @staticmethod
        def is_dict(var):
            if type(var) == dict:
                return True
            else:
                return False

        @staticmethod
        def is_tuple(var):
            if type(var) == tuple:
                return True
            else:
                return False

        @staticmethod
        def is_function(var):
            if callable(var):
                return True
            else:
                return False

    class amount:
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
    class check:
        @staticmethod
        def is_up(url):
            return url

        @staticmethod
        def is_down(url):
            return url

    class errors:
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