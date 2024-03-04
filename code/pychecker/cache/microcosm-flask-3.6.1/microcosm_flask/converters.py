"""
Flask path converters.

"""
from flask_uuid import FlaskUUID


def configure_uuid(graph):
    """
    Register the UUID converter.

    """
    return FlaskUUID(graph.flask)
