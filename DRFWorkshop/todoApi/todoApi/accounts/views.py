from django.contrib.auth import get_user_model, authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from todoApi.accounts.serializers import UserSerializer, LoginRequestSerializer, LoginResponseSerializer, \
    LogoutRequestSerializer, LogoutResponseSerializer

UserModel = get_user_model()


class RegisterUserView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@extend_schema(
    tags=['auth'],
    description='Authenticate a user and return access and refresh tokens',
    summary='Login endpoint',
    request=LoginRequestSerializer,
    responses={
        200: LoginResponseSerializer,
        401: 'Invalid username or password'
    }
)
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({
                'error': 'Invalid username or password',
            },
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'Login successful',
        },
            status=status.HTTP_200_OK
        )


@extend_schema(
    tags=['auth'],
    description='Logout a user and blacklist token',
    summary='Logout endpoint',
    request=LogoutRequestSerializer,
    responses={
        200: LogoutResponseSerializer,
        400: 'Invalid or expired token'
    }
)
class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_str = request.data.get('refresh')
            refresh_token = RefreshToken(refresh_str)
            refresh_token.blacklist()

            return Response({
                'message': 'Logout successful'
            }, status=status.HTTP_200_OK)

        except TokenError:
            return Response({
                'message': 'Invalid or expired token'
            }, status=status.HTTP_400_BAD_REQUEST)
