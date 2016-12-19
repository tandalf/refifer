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
        self.assertIn(urls[0], resp[0]["data"]["urls"])

    def tearDown(self):
        self.ref_client.unsubscribe_client()