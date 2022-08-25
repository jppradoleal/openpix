"""
Module: request_options
"""
import uuid

from .config import Config


class RequestOptions:  # pylint: disable=too-many-instance-attributes

    """This object hold all configurations that will be used in ur REST call.

    All here u can customize as well add params in the requisition header (custom_headers)
    """

    __access_token = None
    __connection_timeout = None
    __custom_headers = None
    __max_retries = None

    def __init__(  # pylint: disable=too-many-arguments
        self,
        access_token=None,
        connection_timeout=60.0,
        custom_headers=None,
        max_retries=3,
    ):
        """Initialize

        Args:
            access_token (str, optional): Your User Access Token. Defaults to None.
            connection_timeout (float, optional): Time to timeout the REST call. Defaults to 60.0.
            custom_headers (dict, optional): A Dict with params to be added to the requests params.
            Defaults to None.
            max_retries (int, optional): How many retries must be done in case of fail.
            Defaults to 3.

        Raises:
            ValueError: Param access_token must be a String
            ValueError: Param connection_timeout must be a Float
            ValueError: Param custom_headers must be a Dictionary
            ValueError: Param max_retries must be an Integer
        """

        if access_token is not None:
            self.access_token = access_token
        if connection_timeout is not None:
            self.connection_timeout = connection_timeout
        if custom_headers is not None:
            self.custom_headers = custom_headers
        if max_retries is not None:
            self.max_retries = max_retries

        self.__config = Config()

    def get_headers(self):
        """
        Sets the attribute values of headers
        """
        headers = {"Authorization": "Bearer " + self.__access_token,
                   "x-tracking-id": self.__config.tracking_id,
                   "User-Agent": self.__config.user_agent,
                   "Accept": self.__config.mime_json}

        if self.__custom_headers is not None:
            headers.update(self.__custom_headers)

        return headers

    @property
    def access_token(self):
        """
        Sets the attribute value and validates access_token
        """
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        if not isinstance(value, str):
            raise ValueError("Param access_token must be a String")
        self.__access_token = value

    @property
    def connection_timeout(self):
        """
        Sets the attribute value and validates connection timeout
        """
        return self.__connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, value):
        if not isinstance(value, float):
            raise ValueError("Param connection_timeout must be a Float")
        self.__connection_timeout = value

    @property
    def custom_headers(self):
        """
        Sets the attribute value and validates custom headers
        """
        return self.__custom_headers

    @custom_headers.setter
    def custom_headers(self, value):
        if not isinstance(value, dict):
            raise ValueError("Param custom_headers must be a Dictionary")
        self.__custom_headers = value

    @property
    def max_retries(self):
        """
        Sets the attribute value and validates max retries
        """
        return self.__max_retries

    @max_retries.setter
    def max_retries(self, value):
        if not isinstance(value, int):
            raise ValueError("Param max_retries must be an Integer")
        self.__max_retries = value
