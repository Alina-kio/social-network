from .models import *
from . serializers import *
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from rest_framework import filters
from rest_framework.generics import ListAPIView

from .services import *



class AuthorizationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response({'key': token.key})
        return Response(status=status.HTTP_403_FORBIDDEN)



class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)
        return Response(data={
            'id': user.id,
            'username': user.username
        })


class ProfileAPIViewSet(ModelViewSet):
    queryset = get_userprofile()
    serializer_class = ProfileSerializer



class UserAPIViewSet(ModelViewSet):
    queryset = get_userprofile()
    serializer_class = UserListSerializer


class PostAPIViewSet(ModelViewSet):
    queryset = get_post()
    serializer_class = PostSerializer



class Search1(ListAPIView):
    queryset = User.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


    # permission_classes = (IsAuthenticatedOrReadOnly)

