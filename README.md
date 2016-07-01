# reqres

Very simple python lib for HTTP Request/Response

## Installation

Just copy `reqres.py` file. No dependencies required

## How to use

```python
>>> import requests
>>> import reqres
>>>
>>>
>>>
>>> headers=reqres.get_basic_auth_headers('user','pass')
>>> resp = reqres.HttpRequest("http://example.com", headers=headers).get().send()
>>> resp.body
'{\n"k":"v"\n}'
>>> resp.json_body()
{u'k': u'v'}
>>>
```
