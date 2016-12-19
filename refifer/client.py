"""
Module used for connecting with the ffire server
"""
import json
import uuid

import requests 
from requests.exceptions import HTTPError

from .constants import RETRY_COUNT, BASE_API_ENDPOINT
from .exceptions import RefiferError

class Refifer(object):
    """
    Class used for making api calls to the ffire server for registering
    and pushing events.
    """

    def __init__(self, client_id=None, retry_count=RETRY_COUNT, 
        timeout=None, proxies=None):

        self.client_id = client_id
        self.timeout = timeout
        self.proxies = proxies
        self.retry_count = retry_count
        self.session = requests.Session()

    def _prepare_headers(self, content_type="application/json"):
        return {"Content-Type": content_type, 
            "X-Client-ID": self.client_id}

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

        Args:
            endpoint(str): the url endpoint to make the request on

        Kwargs:
            args(dict): url parameters structured as a dict

            post_args(dict): data to be submitted to the server as form data

            method(str): http method that will be used for the request

        """
        if post_args:
            method = "POST"

        try:
            headers = self._prepare_headers()
            return self.session.request(method, endpoint, params=args, 
                data=post_args, timeout=self.timeout, proxies=self.proxies,
                headers=headers)

        except HTTPError as e:
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
        data = event_registration.event_registration_data()

        try:
            return self.request(BASE_API_ENDPOINT + "/notifications",
                post_args=json.dumps(data), method="POST")
        except HTTPError as e:
            raise RefiferError(e)


    def fire_event(self, event, transaction_ref=None):
        """
        Publishes an event to the server providing the payload that should
        be broadcasted to the registed endpoints for the event.
        """
        data = event.get_data()
        data_ref = data.get("transaction_reference", None)
        ref = data_ref if data_ref else transaction_ref
        if not ref:
            ref = uuid.uuid4()

        data["transaction_reference"] = ref

        try:
            response = self.request(BASE_API_ENDPOINT, post_args=data, 
                method="POST")
        except HTTPError as e:
            raise RefiferError(e)

    def unsubscribe_client(self):
        return self.request(BASE_API_ENDPOINT + "/notifications", method="DELETE")
