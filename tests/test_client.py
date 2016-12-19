from unittest import TestCase
import json

import requests

from refifer.events import Event, EventRegistration
from refifer.client import Refifer

class TestClient(TestCase):

    def setUp(self):
        self.client_id = "wefinmoirg"
        self.ref_client = Refifer(client_id=self.client_id)

    def test_register_event(self):
        event_name = "ordered_delivered"
        urls = ["https://www.meanstack.com/nonsense", 
            "https://www.this.that/note"]

        event_reg = EventRegistration()
        event_reg.make_payload(event_name=event_name, urls=urls)

        
        resp = self.ref_client.register_event(event_reg).content
        print resp
        resp = json.loads(resp)

        self.assertEqual("successful", resp["status"])
        self.assertIn(urls[0], resp["data"][0]["callback_urls"])

    def test_client_registration_data(self):
        event_name = "ordered_delivered"
        urls = ["https://www.meanstack.com/nonsense", 
            "https://www.this.that/note"]

        #assert event not yet registered
        data = self.ref_client.client_registration_data(event_name)
        self.assertEqual(None, data)

        #register event
        event_reg = EventRegistration()
        event_reg.make_payload(event_name=event_name, urls=urls)

        resp = self.ref_client.register_event(event_reg).content
        print resp
        resp = json.loads(resp)

        #assert that getting client registration detail for event now
        #returns data.
        data = self.ref_client.client_registration_data(event_name)
        self.assertIn(urls[0], data["callback_urls"])
        
    def test_fire_event(self):
        event_name = "ordered_delivered"

        payload = {
            "date":"2016-12-23 10:20", 
            "client":"4949392923", 
            "client_id":129392
        }
        event = Event(event_name, payload=payload)

        resp = self.ref_client.fire_event(event).content
        resp = json.loads(resp)
        print resp

        self.assertEqual("success", resp["status"])

    def tearDown(self):
        self.ref_client.unsubscribe_client()