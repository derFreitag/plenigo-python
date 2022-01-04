
import pytest

from src.plenigo.entities.session import Session

def test_create_session(plenigo_client, customer_data):
    session = Session.create(plenigo_client, customer_data)

    assert 'customerSession' in session._data
