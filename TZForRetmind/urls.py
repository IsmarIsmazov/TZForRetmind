from django.contrib import admin
from django.urls import path, include
from .settings.yasg import urlpatterns_swagger as doc
from apps.products.views import Export

urlpatterns = [
          path('export_data_to_export/', Export.as_view()),
          path('admin/', admin.site.urls),
          path('api/', include('apps.products.urls')),
          path('api/users/', include('apps.users.urls'))
      ] + doc
