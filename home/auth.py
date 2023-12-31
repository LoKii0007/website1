from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http.request import HttpRequest

class Email_OR_Username(BaseBackend):
    # get user by user id
    def get_user(self, user_id: int):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None 
        
    # authentication

    def authenticate(self, request, username = None, password = None, email=None):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(username= username) | Q(email= email))
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        