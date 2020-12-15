from rest_framework import routers, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework_jwt.views import (
    obtain_jwt_token,
    verify_jwt_token,
    refresh_jwt_token,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from apps.users.views import UserViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="hwhong API",
        default_version="v1",
        description="hwhong API",
        contact=openapi.Contact(email="hw.hong@haezoom.com"),
    ),
    permission_classes=(permissions.IsAuthenticated,),
    authentication_classes=(BasicAuthentication,),
)

# Setting
router = routers.DefaultRouter(trailing_slash=False)    # 후행슬래시 삭제
router.register(r"users", UserViewSet)


urlpatterns =[
    # This is for restframework jwt
    url(r"^token-auth/", obtain_jwt_token),
    url(r"^token-refresh/", refresh_jwt_token),
    url(r"^token-verify/", verify_jwt_token),
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui",),
    url(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
urlpatterns += router.urls