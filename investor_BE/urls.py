from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from utils.swagger import schema_view


urlpatterns = [
    # Admin Site
    path('admin/', admin.site.urls),

    # Local Apps
    path('account/', include('apps.account.urls')),

    # Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
