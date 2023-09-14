from django.contrib.auth.models import User

class EmailBackend(object):
    def authenticate(self, request=None, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# class EmailBackend():
#     def authenticate(self, request, username, password):
#         try:
#             user = User.objects.get(email=username)
#             if user.check_password(password):
#                 return user
#             return None
#         except User.DoesNotExist:
#             return None

#     def get_user(self, uid):
#         try:
#             return User.objects.get(pk=uid)
#         except User.DoesNotExist:
#             return None