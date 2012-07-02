class HTTPSProxyMiddleware(object):
    """
    Monkey patches request.is_secure() to respect HTTP_X_FORWARDED_PROTO.
    """
    def process_request(self, request):
        request.is_secure = lambda: request.META.get('HTTP_X_FORWARDED_PROTO') == 'https'