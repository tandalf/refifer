from unittest import TestCase
import os
import json

import requests

from refifer.events import Event, EventRegistration
from refifer.client import Refifer

class TestClient(TestCase):

    def setUp(self):
        self.client_id = 78
        self.access_token = os.environ.get("FETCHR_TOKEN", None)
        if self.access_token == None:
            print("Access token not set. Please set the FETCHR_TOKEN" + \
            " environment variable")
        self.ref_client = Refifer(self.access_token)

    def test_register_event(self):
        event_name = "ordered_picked"
        urls = ["https://www.meanstack.com/nonsense", 
            "https://www.this.that/note"]

        event_reg = EventRegistration(client_id=self.client_id)
        event_reg.set_registration_info(event_name=event_name, urls=urls)

        
        resp = self.ref_client.register_event(event_reg).content
        print resp
        resp = json.loads(resp)

        self.assertEqual("success", resp["status"])
        self.assertIn(urls[0], resp["data"][0]["callback_urls"])

    """def test_client_registration_data(self):
        event_name = "ordered_delivered"
        urls = ["https://www.meanstack.com/nonsense", 
            "https://www.this.that/note"]

        #assert event not yet registered
        data = self.ref_client.client_registration_data(event_name, self.client_id)
        self.assertEqual(None, data)

        #register event
        event_reg = EventRegistration(client_id=self.client_id)
        event_reg.set_registration_info(event_name=event_name, urls=urls)

        resp = self.ref_client.register_event(event_reg).content
        print resp
        resp = json.loads(resp)

        #assert that getting client registration detail for event now
        #returns data.
        data = self.ref_client.client_registration_data(event_name, self.client_id)
        self.assertIn(urls[0], data["callback_urls"])
    """

    def get_basic_event(self, client_id):
        event_name = "ordered_picked"

        payload = {
            "date":"2016-12-23 10:20", 
            "client":"4949392923", 
            "client_id":129392
        }
        return Event(event_name, payload, client_id)
        
    def test_fire_event_from_callable(self):
        event = self.get_basic_event(self.client_id)

        resp = self.ref_client(event.name, event.get_data(), 
            event.client_id).content
        resp = json.loads(resp)
        print resp

        self.assertEqual("success", resp["status"])

    def test_fire(self):
        event = self.get_basic_event(self.client_id)
        resp = self.ref_client.fire(event.name, event.get_data(), 
            event.client_id).content
        resp = json.loads(resp)
        print resp

        self.assertEqual("success", resp["status"])

    def test_fire_event(self):
        event = self.get_basic_event(self.client_id)
        resp = self.ref_client.fire_event(event).content
        resp = json.loads(resp)
        print resp

        self.assertEqual("success", resp["status"])

    def tearDown(self):
        self.ref_client.unsubscribe_client(self.client_id)