Vocloud authenticator
=====================

Simple Python module for JupyterHub authentication to vocloud.

Installation
------------

You can install the authenticator by executing the following command::

    pip3 install git+https://github.com/kozajaku/vocloud-authenticator.git#egg=vocloud-authenticator

Required configuration
----------------------

There is only one option that must be passed to the ``VocloudAuthenticator``::

    VocloudAuthenticator.vocloud_url

The parameter specifies the path to the vocloud deployed application together with
scheme (e.g. http/https) and protocol. For example ``https://vocloud-dev.asu.cas.cz/vocloud-betelgeuse`` could
be one valid option setup.

Optional configuration
----------------------

Following two options are necessary only if vocloud application is somehow unexpectedly modified::

    VocloudAuthenticator.token_endpoint_uri

and::

    VocloudAuthenticator.service_name

The first option specifies the api token endpoint on vocloud relatively to the vocloud url option. The second
one specifies name of the service for the service name checking.
