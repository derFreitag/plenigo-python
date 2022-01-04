
import os
from pathlib import Path, PurePath
import sys

import pytest

# The source code we want to test is at `../src/` relative to this config file.
# We could import that code here, but the imports it makes will not work
# because of the unexpected `src` directory. Appending to the path here will
# ensure that a `plenigo` module is visible everywhere as expected.
sys.path.append(str(PurePath(Path(__file__).parent.resolve(), '../src')))

from plenigo.client.http_client import PlenigoApiType
from plenigo.client.http_client import PlenigoHTTPClient

@pytest.fixture
def plenigo_client():
    api_key = os.environ['PLENIGO_API_KEY']
    return PlenigoHTTPClient(PlenigoApiType.STAGE, api_key)

# TODO: This customer data comes from der Freitag tests. We should decide on
# a more general approach for testing in this repo. Should there be customers
# with known, hardcoded ids? For each run of the tests the old users could be
# cleaned up and re-created. But only one set of tests could be run at a time.
# Better to generate new emails / ids each time? But can we be confident that
# those users are cleaned up and won't pollute plenigo's databases over time?
@pytest.fixture
def customer_data():
    return {
        "customerId": "111112",
        "username": "online_subscriber",
        "email": "no-reply+online@freitag.de",
        "language": "en",
    }
