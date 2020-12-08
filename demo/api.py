from rest_framework import routers, permissions
from rest_framework.authentication import BasicAuthentication

from django.conf.urls import url, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns =[
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui",),
    url(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
urlpatterns += router.urls