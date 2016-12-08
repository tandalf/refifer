"""
Exception Module which contains the exceptions that will be raised when
certain problems occur in the library.
"""

class RefiferError(Exception):
    """
    Base exception class which all Exceptions in this library should 
    inherit from.
    """
    pass

class AuthorizationError(RefiferError):
    """
    Exception raised when the client could not be authenticated on the
    server.
    """
    pass

class DuplicateEventError(RefiferError):
    """
    Raised when a duplicate event has been disallowed by the server.
    """
    pass

class ValidationError(RefiferError):
	"""
	Exception raised when the payload of an event fails to pass some
	validation
	"""
	pass
