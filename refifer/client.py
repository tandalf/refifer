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
        return {"Authorization": self.access_token}

    def _make_registration(self, event_name, event_codes):
        """
        register a client to recieve notification for the various event 
        codes
        """
        pass

    def _build_endpoint(self, resource_url=""):
        raise NotImplemetedError("method not implemented")

    def request(self, endpoint, args=None, post_args=None, method=None):
        """
        Makes a request to the notifications api and returns the response.
        if post_args are available, it makes a post request to the server.
        """
        if post_args:
            method = "POST"

        try:
            headers = self._prepare_headers()
            response = self.session.request(method, endpoint, params=args, 
                data=post_args, timeout=self.timeout, proxies=self.proxies,
                headers=headers)

        except requests.HttpError as e:
            response = json.loads(e.read())
            raise RefiferError(response)

    def get_client_registration_data(self, registration_id):
        """
        Gets the events notification registration details from the server.
        Raises ClientNotRegisterError if the client has not reigstered 
        notifications on the server
        """
        endpoint = self._build_endpoint("fetchrnotifications/notificationlist")
        #todo: build args for get request
        args = {"id": registration_id}
        reg_response = self.request(endpoint, args, method="GET")


    def register_event(self, event_registration):
        """
        Registers an event with the server and provides a list of endpoints
        that are to broadcasted to when the event is fired.
        """
        data = event_registration.get_event_registration_data()

        #if client already has registered events notification with the
        #service, update the registration details


    def fire_event(self, event):
        """
        Publishes an event to the server providing the payload that should
        be broadcasted to the registed endpoints for the event.
        """
        raise NotImplemetedError("method not yet implemented")
