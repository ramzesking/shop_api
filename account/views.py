from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from shop_api.tasks import send_email_task
from django.contrib.auth import get_user_model
from . import serializers
from .send_email import send_confirmation_email

User = get_user_model()


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                # send_confirmation_email(user)#просто отправка без параллелности 
                send_email_task.delay(user.email, user.activation_code)
            return Response(serializer.data, status=201)
        return Response(status=400)


class ActivationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({
                'msg': 'Successfully activated!'},
                status=200)
        except User.DoesNotExist:
            return Response(
                {'msg': 'Link expired!'},
                status=400
            )


class LoginApiView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer


class LogoutApiView(GenericAPIView):
    serializer_class = serializers.LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully loged out', status=204)


class FollowSpamApi(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializer = serializers.SpamViewSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Followed to spam', status=200)

