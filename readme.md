REFIFER
=======

Refifer is an event driven programming library for python, java, and PHP.


## Installation

```shell

pip install refifer

```

## Creating and Firing Events

```python


#: Usage

from refifer.client import Refifer

#: Instantiate Refifer with an auth token 
ref = Refifer("authorization token")

#: application logic for creating payload
payload = {"order_id": "abcd", "client_id": "1234"}

#: push/fire an event to the desired endpoint
#: it is advisable to use constants i.e. ACCOUNT_CREATED, ORDER_SENT
ref.fire("event_name", payload, "client_id")

```


## Subscribing to events

Not yet implemented for refifer