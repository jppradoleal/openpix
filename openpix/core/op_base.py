import json
from openpix.config import Config, RequestOptions


class OPBase:
    def __init__(self, request_options, http_client):
        if not isinstance(request_options, RequestOptions):
            raise ValueError("Param request_options must be a RequestOptions Object")

        self.__request_options = request_options
        self.__http_client = http_client
        self.__config = Config()

    def __check_request_options(self, request_options):
        if request_options is not None and not isinstance(
            request_options, RequestOptions
        ):
            raise ValueError("Param request_options must be a RequestOptions Object")
        if request_options is None:
            request_options = self.__request_options

        if request_options.access_token is None:
            request_options.access_token = self.__request_options.access_token

        return request_options

    def __check_headers(self, request_options, extra_headers=None):
        headers = self.__request_options.get_headers()
        if request_options is not None:
            headers = request_options.get_headers()

        if extra_headers is not None:
            headers.update(extra_headers)

        return headers

    def _get(self, uri, filters=None, request_options=None):
        if filters is not None and not isinstance(filters, dict):
            raise ValueError("Filters must be a Dictionary")

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(
            request_options, {"Content-type": self.__config.mime_json}
        )

        return self.__http_client.get(
            url=self.__config.api_base_url + uri,
            params=filters,
            headers=headers,
            timeout=request_options.connection_timeout,
            maxretries=request_options.max_retries,
        )

    def _post(self, uri, data=None, params=None, request_options=None):
        if data is not None:
            data = json.dumps(data)

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(
            request_options, {"Content-type": self.__config.mime_json}
        )

        return self.__http_client.post(
            url=self.__config.api_base_url + uri,
            data=data,
            params=params,
            headers=headers,
            timeout=request_options.connection_timeout,
            maxretries=request_options.max_retries,
        )

    def _put(self, uri, data=None, params=None, request_options=None):
        if data is not None:
            data = json.dumps(data)

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(
            request_options, {"Content-type": self.__config.mime_json}
        )

        return self.__http_client.put(
            url=self.__config.api_base_url + uri,
            data=data,
            params=params,
            headers=headers,
            timeout=request_options.connection_timeout,
            maxretries=request_options.max_retries,
        )

    def _delete(self, uri, params=None, request_options=None):
        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options)

        return self.__http_client.delete(
            url=self.__config.api_base_url + uri,
            params=params,
            headers=headers,
            timeout=request_options.connection_timeout,
            maxretries=request_options.max_retries,
        )

    @property
    def request_options(self):
        """
        Returns the attribute value of the function
        """
        return self.__request_options

    @property
    def config(self):
        """
        Returns the attribute value of the function
        """
        return self.__config
