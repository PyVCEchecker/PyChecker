"""
Audit log control decorators.

"""
from functools import wraps

from flask import g


def hide(*keys):
    """
    Hide a set of request and/or response fields from logs.

    Example:

        @hide("id")
        def create_foo():
            return Foo(id=uuid4())

    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            g.hide_request_fields = keys
            g.hide_response_fields = keys
            return func(*args, **kwargs)
        return wrapper
    return decorator


def show_as(**mappings):
    """
    Show a set of request and/or response fields in logs using a different key.

    Example:

        @show_as(id="foo_id")
        def create_foo():
            return Foo(id=uuid4())

    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            g.show_request_fields = mappings
            g.show_response_fields = mappings
            return func(*args, **kwargs)
        return wrapper
    return decorator
