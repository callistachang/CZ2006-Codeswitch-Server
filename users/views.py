from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .models import ModifiedUser
from .serializers import UserSerializer

from utils import get_or_none

@csrf_exempt
def login_view(request):
    input_email = request.POST.get('email')
    input_password = request.POST.get('password')

    status_code = 403
    message = 'Email not found'

    user = get_or_none(ModifiedUser, email=input_email)
    if user:
        if check_password(input_password, user.password):
            status_code = 200
            message = 'Login successful'
        else:
            message = 'Wrong password'
    
    return JsonResponse({'status_code': status_code, 'message': message})

class UserViewSet(viewsets.ModelViewSet):
    queryset = ModifiedUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer