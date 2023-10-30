from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Investor BE",
        default_version="v1",
        description="Your API Description",
    ),
    public=True,
    permission_classes=[AllowAny]
)
