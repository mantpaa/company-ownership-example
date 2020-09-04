from flask import url_for
from main import app

CANICA_AS = "891450052"

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
