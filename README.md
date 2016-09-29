# reqres

[![Build Status](https://travis-ci.org/ownport/reqres.svg?branch=master)](https://travis-ci.org/ownport/reqres)
[![codecov](https://codecov.io/gh/ownport/reqres/branch/master/graph/badge.svg)](https://codecov.io/gh/ownport/reqres)

Very simple python lib for HTTP Request/Response

## Installation

Just copy `reqres.py` file. No dependencies required

## How to use

```python
>>> import reqres
>>> headers=reqres.get_basic_auth_headers('user','pass')
>>> resp = reqres.Request("http://example.com", headers=headers).get().send()
>>> resp.body
'{\n"k":"v"\n}'
>>> resp.json_body()
{u'k': u'v'}
>>>
```

## For developers

```sh
$ make run-local-ci
.....
[INFO] Cleaning directory: /repo/.local-ci
[INFO] Cleaning directory: /repo/reqres.egg-info
[INFO] Cleaning files: *.pyc
[INFO] Cleaning files: .coverage
============================= test session starts ==============================
platform linux2 -- Python 2.7.12, pytest-3.0.2, py-1.4.31, pluggy-0.3.1
rootdir: /repo, inifile:
plugins: cov-2.3.1
collected 12 items

tests/test_reqres.py ............

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name        Stmts   Miss  Cover   Missing
-----------------------------------------
reqres.py      62      0   100%


========================== 12 passed in 0.32 seconds ===========================
```
