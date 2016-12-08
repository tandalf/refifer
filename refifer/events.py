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



def picked_validator(event):
    """
    validator used for validating the fields of a `picked` event
    """
    payload = event.payload
    if payload["status_code"] != "PCK":
        raise ValidationError("Status code for payload should be PCK.")

    if payload["status_name"] != "Picked":
        raise ValidationError("Status name is incorrect")