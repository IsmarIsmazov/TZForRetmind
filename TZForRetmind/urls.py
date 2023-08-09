from django.contrib import admin
from django.urls import path, include
from .settings.yasg import urlpatterns_swagger as doc

urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/', include('apps.products.urls')),
      path('api/', include('apps.users.urls'))
] + doc
