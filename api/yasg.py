from django.conf.urls import url
from django.urls import path, include
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_url_patterns = [
    path('api/', include('api.urls')),
]
 
schema_view = get_schema_view(
    openapi.Info(
        title="DRF API Documents",
        default_version='v1',
        description = "DjangoRestFramework API Server",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="park19996@gmail.com"),
        license=openapi.License(name="ParkHyeonChae"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns,
)