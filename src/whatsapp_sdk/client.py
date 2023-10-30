import logging
import urllib.parse
from platform import python_version

from requests import Response
from requests.adapters import HTTPAdapter
from requests.sessions import Session

from .. import whatsapp_sdk
from .error import *
from .whatsapp import Whatsapp
from .schema.response import WAResponse

log = logging.getLogger(__name__)

try:
    from json import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


class Client:

    def __init__(
            self,
            api_token,
            phone_number_id,
            version="v17.0",
            timeout=30,
            pool_connections=10,
            pool_maxsize=10,
            max_retries=3,
            **kwargs
    ) -> None:
        self._api_token = api_token
        self._version = version
        self._phone_number_id = phone_number_id

        self._scheme = "https"

        self._host = "graph.facebook.com"

        user_agent = f"whatsapp-sdk/{whatsapp_sdk.__version__} python/{python_version()}"

        self.headers = {
            "User-Agent": user_agent,
            "Accept": "application/json",
        }
        self.whatsapp = Whatsapp(self)

        self.timeout = timeout
        self.session = Session()
        self.adapter = HTTPAdapter(
            pool_connections=pool_connections,
            pool_maxsize=pool_maxsize,
            max_retries=max_retries,
        )
        self.session.mount("https://", self.adapter)

    def _create_bearer_token_string(self):
        return f"Bearer {self._api_token}"

    # Gets and sets _host attribute
    def host(self, value=None):
        if value is None:
            return self._host
        else:
            self._host = value

    def _create_request_url(self, host=None, path=None):
        # if host:
        #     _host = host
        # else:
        #     _host = self._host
        # if path:
        #     _path = path
        # else:
        #     _path = "/messages"
        # return f"{_host}/{self._version}/{self._phone_number_id}{path}"
        path = path or "/messages"
        url_path = f"/{self._version}/{self._phone_number_id}{path}"
        url_parts = (self._scheme, host or self._host, url_path, None, None, None)
        return urllib.parse.urlunparse(url_parts)

    @staticmethod
    def process_response(host, response: Response):
        """
        Process the response from the D7 API.
        """
        log.debug(f"Response headers {repr(response.headers)}")
        if response.status_code == 401:
            log.warning(f"Authentication error: {response.status_code} {repr(response.content)}")
            return WAResponse(**response.json())
            # raise AuthenticationError("Invalid API token")
        elif 200 <= response.status_code < 300:
            # success response
            try:
                result = response.json()
                log.debug(f"Successful process response: {result}")
                return WAResponse(**result)
            except JSONDecodeError:
                pass
        elif 400 <= response.status_code < 500:
            log.warning(f"Client error: {response.status_code} {repr(response.content)}")
            return WAResponse(**response.json())
            # if response.status_code == 400:
            #     return WAResponse(**response.json())
            #     # raise BadRequest(f"{repr(response.content)}")
            # if response.status_code == 404:
            #     # raise NotFoundError(f"{repr(response.content)}")
            # if response.status_code == 402:
            #     raise InsufficientCreditError(f"{repr(response.content)}")
            # if response.status_code == 422:
            #     raise ValidationError(f"{repr(response.content)}")
            # else:
            #     raise ClientError(f"{response.status_code} response from {host}")
        elif 500 <= response.status_code < 600:
            log.warning(f"Server error: {response.status_code} {repr(response.content)}")
            message = f"{response.status_code} response from {host}"
            raise ServerError(message)

    def get(self, host=None, path="messages", params=None):
        """
        Send HTTP POST request to the D7 API.
        """
        # "https://graph.facebook.com/v17.0/140464972481061/messages"
        request_url = f"{self._host}/{self._version}/{self._phone_number_id}/{path}"
        self._request_headers = self.headers
        self._request_headers['Authorization'] = self._create_bearer_token_string()
        log.debug(f"GET request sent to {request_url} with headers {self._request_headers} and params {params}")
        return self.process_response(host,
                                     self.session.get(
                                         request_url,
                                         headers=self._request_headers,
                                         params=params,
                                         timeout=self.timeout
                                     )
                                     )

    def post(self, host=None, path=None, body_is_json=True, params={}):
        """
        Send HTTP POST  request to meta whatsapp cloud api
        """
        request_url = self._create_request_url(host=host, path=path)
        print(f"Request URL: {request_url}")
        self._request_headers = self.headers
        self._request_headers['Authorization'] = self._create_bearer_token_string()
        if body_is_json:
            self._request_headers['Content-Type'] = 'application/json'
            log.debug(f"POST request sent to {request_url} with headers {self._request_headers} and params {params}")
            return self.process_response(host,
                                         self.session.post(
                                             request_url,
                                             headers=self._request_headers,
                                             json=params,
                                             timeout=self.timeout
                                         )
                                         )
        else:
            self._request_headers['Content-Type'] = 'application/x-www-form-urlencoded'
            return self.process_response(host,
                                         self.session.post(
                                             request_url,
                                             headers=self._request_headers,
                                             data=params,
                                             timeout=self.timeout
                                         )
                                         )

    def put(self, path, data=None):
        ...

    def delete(self, path, data=None):
        ...

    def patch(self, path, data=None):
        ...
