from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Advertisment API",
        default_version='v1',
        description="API для управления объявлениями",
        terms_of_service="https://localhost:8000/terms/",
        contact=openapi.Contact(email="support@yourapp.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)