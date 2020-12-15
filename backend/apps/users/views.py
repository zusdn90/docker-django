from django.shortcuts import render

from rest_framework import viewsets, status, views, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authentication import BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from apps.users.models import User
from apps.users.serializers import UserSerializer, AuthSerializer
from apps.core.utils import get_now
from apps.core import message as msg

import logging

LOGGER = logging.getLogger("default")
LOGGER.name == __name__

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticated,) # tuple 사용 시 element가 1개일 경우 마지막에 ,를 붙여야 인식한다.
    authentication_classes = (JSONWebTokenAuthentication, BasicAuthentication)
    
    def retrieve(self, request: Request, pk: str) -> Response:
        try:
            user = self.get_object()
            assert user.id == request.user.id
        except Exception as e:
            LOGGER.error("Exception Error : " + str(e))
            dict = {
                "status": "error",
                "code": status.HTTP_400_BAD_REQUEST,
                "message": msg.REQUEST_FAIL,
            }
            return Response(dict, status=status.HTTP_400_BAD_REQUEST)

        serializaer = self.serializer_class(user)
        return Response({"result": serializaer.data}, status=status.HTTP_200_OK)