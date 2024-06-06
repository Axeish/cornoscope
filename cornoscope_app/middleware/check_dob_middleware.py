# myapp/middleware/check_dob_middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class CheckDOBMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = [reverse('index'), reverse('too_young')]
        if request.path not in allowed_paths and 'date_of_birth' not in request.session:
            return redirect('index')
        return self.get_response(request)
