
import pytest
import reqres
import urllib2

import cStringIO

# -------------------------------------------------------------------
#
#   Mocks
#
class MockedResponse(object):

    def __init__(self):
        self.mocked_response = 'MockedResponse.read()'
        self.read_count = 0

    def read(self, size=0):
        result = self.mocked_response
        if self.read_count > 0:
            result = None
        self.read_count += 1
        return result

    def info(self):
        return {'type': 'MockedResponse'}


class MockedOpener(object):

    def __init__(self, handler):
        self._handler = handler

    def open(self, request, timeout):
        if request.get_full_url() == 'http://non-exists.com':
            raise urllib2.HTTPError(
                    url=request.get_full_url(),
                    code=500,
                    msg='The host does not exist, %s' % request.get_full_url(),
                    hdrs={},
                    fp=cStringIO.StringIO()
            )
        return MockedResponse()

# -------------------------------------------------------------------
#
#   Tests: Exception
#
def test_httpexception():

    e = reqres.HTTPException(code=200, msg='OK', headers={'k1':'v1'}, body=None)
    assert isinstance(e, reqres.HTTPException)
    assert e.code == 200
    assert e.msg == 'OK'
    assert e.headers == {'k1':'v1'}
    assert e.body == None

# -------------------------------------------------------------------
#
#   Tests: Response
#
def test_httpresponse():

    resp = reqres.Response(code=200, headers={'k1':'v1'}, body='{}', error_msg=None)
    assert isinstance(resp, reqres.Response)
    assert resp.code == 200
    assert resp.headers == {'k1':'v1'}
    assert resp.body == '{}'
    assert resp.error_msg == None
    assert resp.json_body() == {}


def test_httpresponse_jsonbody():

    resp = reqres.Response(code=200, headers={'k1':'v1'}, body='{}', error_msg=None)
    assert resp.json_body() == {}

# -------------------------------------------------------------------
#
#   Tests: Request
#
def test_httprequest_create(monkeypatch):

    monkeypatch.setattr("urllib2.build_opener", lambda h: MockedOpener(h))

    req = reqres.Request('http://example.com', headers={'k1':'v1'})
    assert isinstance(req, reqres.Request)
    assert req.headers == {'k1':'v1'}


def test_httprequest_get(monkeypatch):

    monkeypatch.setattr("urllib2.build_opener", lambda h: MockedOpener(h))

    req = reqres.Request('http://example.com', headers={'k1':'v1'})
    resp = req.get().send()
    assert isinstance(resp, reqres.Response)
    assert resp.body == 'MockedResponse.read()'

def test_httprequest_failed_request(monkeypatch):

    monkeypatch.setattr("urllib2.Request", lambda url, data: None)
    req = reqres.Request('http://example.com')
    with pytest.raises(RuntimeError):
        req.get()

def test_httprequest_post(monkeypatch):

    monkeypatch.setattr("urllib2.build_opener", lambda h: MockedOpener(h))

    req = reqres.Request('http://example.com', headers={'k1':'v1'})
    resp = req.post().send()
    assert isinstance(resp, reqres.Response)
    assert resp.body == 'MockedResponse.read()'


def test_httprequest_put(monkeypatch):

    monkeypatch.setattr("urllib2.build_opener", lambda h: MockedOpener(h))

    req = reqres.Request('http://example.com', headers={'k1':'v1'})
    resp = req.put().send()
    assert isinstance(resp, reqres.Response)
    assert resp.body == 'MockedResponse.read()'


def test_httprequest_patch(monkeypatch):

    monkeypatch.setattr("urllib2.build_opener", lambda h: MockedOpener(h))

    req = reqres.Request('http://example.com', headers={'k1':'v1'})
    resp = req.patch().send()
    assert isinstance(resp, reqres.Response)
    assert resp.body == 'MockedResponse.read()'


def test_httprequest_get_stream(monkeypatch):

    monkeypatch.setattr("urllib2.build_opener", lambda h: MockedOpener(h))

    req = reqres.Request('http://example.com', headers={'k1':'v1'})
    resp = req.get().send(stream=True)
    assert isinstance(resp, reqres.Response)
    body = ''
    while  True:
        chunk = resp.body.read(64000)
        if not chunk:
            break
        body += chunk
    assert body == 'MockedResponse.read()'


def test_httprequest_get_error(monkeypatch):

    monkeypatch.setattr("urllib2.build_opener", lambda h: MockedOpener(h))

    URL = 'http://non-exists.com'

    req = reqres.Request(URL)
    resp = req.get().send()
    assert isinstance(resp, reqres.Response)
    assert resp.code == 500
    assert resp.error_msg == 'The host does not exist, %s' % URL

# -------------------------------------------------------------------
#
#   Tests: utils
#

def test_basic_auth_headers():

    assert reqres.get_basic_auth_headers('u1', 'p1') == {'Authorization': 'Basic dTE6cDE='}
