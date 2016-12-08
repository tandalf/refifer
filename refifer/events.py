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
    """

    def __init__(self, client_id, webhook_url="", phone="", email="", 
        event_codes=[]):

        self.client_id = client_id
        self.webhook_url = webhook_url
        self.phone = phone
        self.email = email
        self.status_codes = status_codes
        self._event_codes = event_codes

    def add_event_by_code(self, event_code):
        """
        Adds an event code the lis t events that are to be registered.
        """

        #perform some checks if neccesary in cases where conflicts may 
        #arise
        self._event_codes.append(event_code)

    def get_event_registration_data(self):

        payload = {
                    "clientWebhookUrl":self.webhook_url, "email": self.email,
        }

        for code in self._event_codes:
            if code == "order_uploaded":
                payload.setdefault("SU1", "order_uploaded")
            elif code == "order_picked":
                payload.setdefault("SU2", "order_picked")
            elif code == "order_scheduled":
                payload.setdefault("SU3", "order_scheduled")
            elif code == "order_recieved":
                payload.setdefault("SU4", "order_recieved")

        return payload

def picked_validator(event):
    """
    validator used for validating the fields of a `picked` event
    """
    payload = event.payload
    if payload["status_code"] != "PCK":
        raise ValidationError("Status code for payload should be PCK.")

    if payload["status_name"] != "Picked":
        raise ValidationError("Status name is incorrect")