from openpix.core import HttpClient
from openpix.config import RequestOptions


class SDK:
    def __init__(
        self,
        access_token,
        http_client=None,
        request_options=None,
    ):
        """Construct ur SDK Object to have access to all APIs modules.
        Args:
            [Click here for more info](https://developers.openpix.com.br/docs/apis/api-getting-started/#criando-uma-nova-chave-de-apiplugin)
            http_client (openpix.http.http_client, optional): An implementation of
            HttpClient can be pass to be used to make the REST calls. Defaults to None.
            request_options (openpix.config.request_options, optional): An instance
            of RequestOptions can be pass changing or adding custom options to ur REST
            calls. Defaults to None.
        Raises:
            ValueError: Param request_options must be a RequestOptions Object
        """

        self.http_client = http_client
        if http_client is None:
            self.http_client = HttpClient()

        self.request_options = request_options
        if request_options is None:
            self.request_options = RequestOptions()

        self.request_options.access_token = access_token
