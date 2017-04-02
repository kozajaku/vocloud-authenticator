from jupyterhub.auth import Authenticator
from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPError
from traitlets import Unicode
from urllib.parse import urlencode
import json


class VocloudAuthenticator(Authenticator):
    vocloud_url = Unicode(
        config=True,
        help="""
        URL to the running vocloud instance together with scheme and port.
        E.g. https://vocloud-dev.asu.cas.cz/vocloud-betelgeuse
        """
    )

    token_endpoint_uri = Unicode(
        config=True,
        default='/api/jupyter/token',
        help="""
        URI to the vocloud token endpoint relative to vocloud URL context
        """
    )

    service_name = Unicode(
        config=True,
        default='jupyterhub',
        help="""
        Expected service name. This name should come from the vocloud token endpoint
        and must be validated against.
        """
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data.get('username')
        password = data.get('password')
        if username is None or password is None:
            return None
        if password.strip() == '':
            return None
        while self.vocloud_url.endswith('/'):
            self.vocloud_url = self.vocloud_url[0: -1]
        while self.token_endpoint_uri.startswith('/'):
            self.token_endpoint_uri = self.token_endpoint_uri[1:]
        url = "{}/{}".format(self.vocloud_url, self.token_endpoint_uri)
        data = urlencode({'token': password})
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        client = AsyncHTTPClient()
        request = HTTPRequest(url, method='POST', headers=headers, body=data)
        try:
            response = yield client.fetch(request)
            res = json.loads(response.body.decode('utf-8'))
            if username != res.get('username'):
                return None
            # check service name
            if self.service_name != res.get('serviceName'):
                return None
            return username  # authentication successful
        except HTTPError:
            return None
