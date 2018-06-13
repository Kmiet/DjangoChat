from django.http import HttpResponseRedirect
from django.conf import settings

class RoutingMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path.lstrip('/')
        print(path)
        if request.user.is_authenticated:
            if path == 'login/' or path == 'register/':
                return HttpResponseRedirect('/lobby')
        else:
            if path != 'login/' and path != 'register/':
                return HttpResponseRedirect('/login')

        return None