class HTTPSProxyMiddleware(object):
    """
    Monkey patches request.is_secure() to respect HTTP_X_FORWARDED_PROTO.
    """
    def process_request(self, request):
        if 'HTTP_X_FORWARDED_PROTO' in request.META:
            request.is_secure = lambda: request.META['HTTP_X_FORWARDED_PROTO'] == 'https'