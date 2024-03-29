from django.contrib import admin
from django.urls import path, include, re_path
from bringel import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

schema_view = get_schema_view(
    openapi.Info(
        title="Bringel Store API",
        default_version='v1',
        description="API de acesso à API da Bringel Store",
        contact=openapi.Contact(name="José Ari Junior",
                                email="josearijunior@hotmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.welcome, name='welcome'),
    path('celery-test', views.CeleryAPIListView.as_view(), name='celery-test'),
    path('error', views.error),

    path('client/', include('client.urls')),
    path('product/', include('product.urls')),


]

# swagger
urlpatterns += [

   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # noqa E501
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # noqa E501
   path('redoc/', schema_view.with_ui('redoc',
        cache_timeout=0), name='schema-redoc'),
]

# JWT
urlpatterns += [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # noqa E501
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # noqa E501
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
