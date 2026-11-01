from typing import Any


class validations:
    """Collection of value validation utilities."""

    class type:
        """Type validation utilities."""

        @staticmethod
        def is_int(var: Any) -> bool:
            return type(var) is int

        @staticmethod
        def is_string(var: Any) -> bool:
            return type(var) is str

        @staticmethod
        def is_float(var: Any) -> bool:
            return type(var) is float

        @staticmethod
        def is_list(var: Any) -> bool:
            return type(var) is list

        @staticmethod
        def is_bool(var: Any) -> bool:
            return type(var) is bool

        @staticmethod
        def is_dict(var: Any) -> bool:
            return type(var) is dict

        @staticmethod
        def is_tuple(var: Any) -> bool:
            return type(var) is tuple

        @staticmethod
        def is_function(var: Any) -> bool:
            return callable(var)

    class amount:
        """Value presence validation utilities."""

        @staticmethod
        def is_set(var: Any) -> bool:
            return var is not None

        @staticmethod
        def is_empty(var: Any) -> bool:
            return var is None

    class numbers:
        """Numeric comparison validation utilities."""

        @staticmethod
        def is_positive(var: int | float) -> bool:
            return var > 0

        @staticmethod
        def is_negative(var: int | float) -> bool:
            return var < 0

        @staticmethod
        def is_zero(var: int | float) -> bool:
            return var == 0
