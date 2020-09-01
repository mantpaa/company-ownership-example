import pytest

from flask import url_for

from main import app

CANICA_AS = "891450052"


@pytest.fixture
def client():
    app.config['TESTING'] = True

    ctx = app.test_request_context()
    ctx.push()

    return app.test_client()


@pytest.mark.parametrize("orgnr", [
    "1",
    "s",
    "12345678",
    "1234567890",
    "1abc1",
    "1abc",
    "abc1",
    "too_long_orgnr",
    "s123456789s"
])
def test_invalid_orgnr(orgnr, client):

    urls = [
        "%s/owners" % orgnr,
        "%s/holdings" % orgnr,
        "%s/summary" % orgnr
    ]

    for url in urls:
        response = client.get(url)
        assert response.status_code == 400, "%r should return 400 BAD REQUEST" % url


def test_owners(client):
    url = url_for('owners', orgnr=CANICA_AS)
    response = client.get(url)
    assert response.status_code == 200


def test_holdings(client):
    url = url_for('holdings', orgnr=CANICA_AS)
    response = client.get(url)
    assert response.status_code == 200


def test_summary(client):
    url = url_for('summary', orgnr=CANICA_AS)
    response = client.get(url)
    assert response.status_code == 200
