"""
Module used for connecting with the ffire server
"""
import requests 

from .constants import RETRY_COUNT

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

    def request(self, endpoint, args=None, post_args=None, method=None):
        """
        Makes a request to the notifications api and returns the response.
        if post_args are available, it makes a post request to the server.
        """
        if post_args:
            method = "POST"

    def register_event(self, event_name, endpoints):
        """
        Registers an event with the server and provides a list of endpoints
        that are to broadcasted to when the event is fired.
        """
        raise NotImplemetedError("method not yet implemented")

    def publish_event(self, event_name, payload):
        """
        Publishes an event to the server providing the payload that should
        be broadcasted to the registed endpoints for the event.
        """
        raise NotImplemetedError("method not yet implemented")