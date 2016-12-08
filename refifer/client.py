"""
Module used for connecting with the ffire server
"""
import json

import requests 

from .constants import RETRY_COUNT, BASE_API_ENDPOINT
from .exceptions import RefiferError

class Refifer(object):
    """
    Class used for making api calls to the ffire server for registering
    and pushing events.
    """

    def __init__(self, access_token=None, retry_count=RETRY_COUNT, 
        timeout=None, proxies=None):

        self.access_token = access_token
        self.timeout = timeout
        self.proxies = proxies
        self.retry_count = retry_count
        self.session = requests.Session()

    def _prepare_headers(self):
        return {"access_token": self.access_token}

    def _make_registration(self, event_name, event_codes):
        """
        register a client to recieve notification for the various event 
        codes
        """
        pass

    def request(self, endpoint, args=None, post_args=None, method=None):
        """
        Makes a request to the notifications api and returns the response.
        if post_args are available, it makes a post request to the server.
        """
        if post_args:
            method = "POST"

        try:
            response = self.session.request(method, endpoint, params=args, 
                data=post_args, timeout=self.timeout, proxies=self.proxies)

        except requests.HttpError as e:
            response = json.loads(e.read())
            raise RefiferError(response)


    def register_event(self, event_registration):
        """
        Registers an event with the server and provides a list of endpoints
        that are to broadcasted to when the event is fired.
        """
        raise NotImplemetedError("method not yet implemented")

    def fire_event(self, event):
        """
        Publishes an event to the server providing the payload that should
        be broadcasted to the registed endpoints for the event.
        """
        raise NotImplemetedError("method not yet implemented")
