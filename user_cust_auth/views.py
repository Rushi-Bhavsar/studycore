from django.contrib.auth import get_user_model
from rest_framework import views, viewsets, status
from rest_framework.response import Response
from django.conf import settings

from .models import StudentInfo
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
UserModel = get_user_model()


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class StudentSession(viewsets.ModelViewSet):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class CreateSession(views.APIView):
    # We need CSRF-Token in case of POST, PUT, DELETE, UPDATE method if we are using cookies while send request.
    # The CSRF Token needs to be set in cookies as "csrftoken" and "X-CSRFToken" in headers.
    # https://stackoverflow.com/questions/30871033/django-rest-framework-remove-csrf
    # By default, Django uses SessionAuthentication as DEFAULT_AUTHENTICATION_CLASSES.
    # If we want to disable the csrf validation we need to set authentication_class as empty or anything other than \
    # SessionAuthentication.
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = UserModel.objects.get_by_natural_key(username)
        if user and user.check_password(password):
            # If we want to use default session-authentication class then we need to set below keys as a encoded values
            # in the session table.
            user_hash = user.get_session_auth_hash()
            request.session['_auth_user_id'] = str(user.pk)
            request.session['_auth_user_backend'] = settings.AUTHENTICATION_BACKENDS[0]
            request.session['_auth_user_hash'] = user_hash
            return Response(data={'key': 'Success'}, status=status.HTTP_200_OK)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(views.APIView):
    # This View create a new CSRFToken and set it in the user-agent(client browser, postman, client app)
    # The token created needs to be set in cookies as well as "X-CSRFToken" in headers.

    def get(self, request):
        return Response(data={"Key": "CSRF_COOKIE SET"})
