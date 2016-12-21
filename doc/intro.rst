Introduction
============

Refifer is a client library basically used for pushing events to fetchr's events 
service and registering event callbacks on it's notification service.

Installation
------------
To install *refifer*, on your terminal enter

.. code-block:: bash

   $ pip install refifer

This installs refifer and it's dependencies. If you need to build this documentation,
then you have to install the requirements in *requirements-dev.txt*

Using Refifer
-------------

The Refifer client class from the refifer.client module can be used to fire
an event and must be initialized with an access_token. Example usage:

.. code-block:: python

   from refifer import Refifer
   
   ref = Refifer("bad_access_token")

   payload = {"client_name": ...}

   # the client_id of the client the request is to be made on behalf of
   client_id = "Fetchr"

   #fire an event with payload
   ref.fire("event_name", payload, client_id)

The Refifer class can also be explicitly imported from the client module, e.g,

.. code-block:: python
   
   from refifer.client import Refifer