"""
Module used for connecting with the ffire server
"""
from requests import session, Request

from .constants import RETRY_COUNT

class Refifer(object):
	"""
	Class used for making api calls to the ffire server for registering
	and pushing events.
	"""

	def __init__(self, username=None, password=None, access_token=none, 
		retry_count=RETRY_COUNT, timeout=None, proxies=none):
	
		self.username = username
		self.password = password
		self.timeout = timeout
		self.proxies = proxies
		self.retry_count = retry_count

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