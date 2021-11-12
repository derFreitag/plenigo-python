from collections import OrderedDict
from datetime import datetime

from plenigo.client.http_client import HTTPClient, Sorting
from plenigo.resources.deletable_resource import APIDeletableResource
from plenigo.resources.resource import APIResource
from plenigo.resources.searchable_resource import APISearchableResource


class Session(APIResource):
    """
    Represents a session.
    """

    def __init__(self, http_client: HTTPClient, data: OrderedDict):
        super(Session, self).__init__(http_client, data)

    def get_id(self) -> any:
        if self._data is not None and "sessionId" in self._data:
            return self._data["sessionId"]
        return ""

    @staticmethod
    def _get_entity_url_part() -> str:
        return "sessions"

    @staticmethod
    def _create_instance(http_client: HTTPClient, data: OrderedDict) -> any:
        return Session(http_client, data)

    @staticmethod
    def validate(http_client: HTTPClient, sessionToken: str) -> any:
        """
        Check if a session is currently valid
        :param sessionToken: The token for the session you would like to validate
        :return: detailed information about the session including the customerId
        """
        return http_client.get(url="sessions/validate", params={"sessionToken": sessionToken})

    @staticmethod
    def customer_data(http_client: HTTPClient, sessionToken: str) -> any:
        """
        Fetch the customer data for a valid session token
        :param sessionToken: The token for the customer's session
        :return: detailed customer information including email
        """
        return http_client.get(url="sessions/customerData", params={"sessionToken": sessionToken})
