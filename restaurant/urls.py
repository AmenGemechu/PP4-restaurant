from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('exotic_cuisine.urls', namespace='exotic_cuisine')),
    path('summernote/', include('django_summernote.urls')),
]
