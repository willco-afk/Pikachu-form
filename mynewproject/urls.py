from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Keep this line
    # Remove the GLTF serving path:
    # path('gltf/<path:path>/', serve_gltf_files, name='serve_gltf_files'),  # Delete this line
]