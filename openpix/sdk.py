from openpix.core import HttpClient
from openpix.config import RequestOptions
from openpix.resources import Charge, Refund, Transaction, Customer


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
            http_client (openpix.core.http_client, optional): An implementation of
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

    def charge(self, request_options=None):
        return Charge(
            request_options is not None and request_options or self.request_options,
            self.http_client,
        )

    def refund(self, request_options=None):
        return Refund(
            request_options is not None and request_options or self.request_options,
            self.http_client,
        )

    def transaction(self, request_options=None):
        return Transaction(
            request_options is not None and request_options or self.request_options,
            self.http_client,
        )

    def customer(self, request_options=None):
        return Customer(
            request_options is not None and request_options or self.request_options,
            self.http_client,
        )
