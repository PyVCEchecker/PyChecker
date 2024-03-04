"""
Support a user-defined per-request session.

"""
from flask import g


def register_session_factory(graph, key, session_factory):
    """
    Register a session creation function so that a new session (of user-defined type)
    will be saved to `flask.g` on every request (and closed on teardown).

    In other words: this os a mechanism to register a SQLAlchemy session instance
    or similar without coupling the web and database tiers directly.

    The session function should have the signature:

        def session_factory(graph):
            return Session()

    If the session instance is closeable, it will be closed on teardown.

    """
    @graph.flask.before_request
    def begin_session():
        setattr(g, key, session_factory(graph))

    @graph.flask.teardown_request
    def end_session(*args, **kwargs):
        # NB: session will be none if there's an error raised in `before_request`
        session = getattr(g, key, None)
        if session is not None and hasattr(session, "close"):
            session.close()
