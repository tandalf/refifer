"""
Module which contains classes and other functionalities for handling 
events
"""

from .exceptions import ValidationError

class Event(object):
    """
    Represents an event that will be sent to the notification service.
    This class uses validators to validate the payload of its instances.

    Validators are callables which takes an event as
    input and raises an exception if the payload could not
    be validated by the callable.
    """

    def __init__(self, name, display_name="", payload={}):
        self.name = name
        self.display_name = display_name
        self.payload = payload
        self._validators = []

    def add_payload_validator(self, validator):
        self._validators.append(validator)

    def clear_validators(self):
        self._validators = []

    def validate(self):
        try:
            for validator in self._validators:
                validator(self)
        except Exception as e:
            raise ValidationError(e)

class EventRegistration(object):
    """
    Class that represents the data used for registering events notification
    on the service.

    The registration payload can be set by users but the payload can also
    be build by adding events to the registration object using the 
    exposed methods.

    Args:
        token(str): the authentication token that will be used to authorize
            and identify a user.

    kwargs:
        registration_payload(dict): an optional keyword arguement that 
        contains the payload that will be posted to the server.

    Todo:
        We need to elaborate more on the formart for the payload. This 
        should be done when the payload has been well specified and 
        documented by the service owners.
    """

    def __init__(self, token, registration_payload={}):
        self.token = token
        self._event_endpoints = registration_payload

    def add_event(self, event_code, url=None, email=None, sms=None):
        """
        Adds an event code to the list of events that are to be registered, 
        including the url, email, or sms number that are to recieve 
        notifications about the event.

        Args:
            event_code(str): the code that uniquely identifies the event.

        Kwargs:
            url(str): (optional) the url for the endpoint that will recieve 
                the event.
            email(str): (optional) the email that will be sent a notification
                when the event is fired.
            sms(str): (optional) the phone number that will be sent a 
                notification when the event is fired.
        """

        #perform some checks if neccesary in cases where conflicts may 
        #arise
        self._event_endpoints.setdefault(event_code, url)
        self._event_endpoints.setdefault(event_code + "url", True)

    def event_registration_data(self):
        """
        Prepares the data that will be posted to the notification
        service given the event codes that have been added to the
        instance.
        """

        payload = self._event_endpoints
        payload.setdefault("token", self.token)

        return payload

def picked_event_validator(event):
    """
    validator used for validating the fields of a `picked` event

    Args:
        event(Event): the event that is to be validated.
    """
    payload = event.payload
    if payload["status_code"] != "PCK":
        raise ValidationError("Status code for payload should be PCK.")

    if payload["status_name"] != "Picked":
        raise ValidationError("Status name is incorrect")