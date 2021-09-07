import abc

from plenigo.client.http_client import HTTPClient
from plenigo.resources.resource import APIResource
from plenigo.resources.searchable_resource import APISearchableResource


class APIUpdatableResource(APISearchableResource, abc.ABC):
    """
    Represents an API entity that can be updated.
    """

    @staticmethod
    def create(http_client: HTTPClient, data: dict) -> any:
        """
        Creates a new instance with the given data.
        :param http_client: http client to use
        :param data: instance data
        :return: instance created
        """
        data = http_client.post(APIResource._get_entity_url_part(), data=data)
        return APIResource._create_instance(http_client, data)

    def update(self) -> any:
        """
        Saves the current instance.
        :return: updated instance
        """
        if self._http_client is None:
            raise ValueError("Instance must be a managed instance.")
        self._data = self._http_client.put(url="%s/%s" % (APIResource._get_entity_url_part(), self.get_id()), data=self._data)
        return self