from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-zimmedar/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),  # Google Auth routes
    path('', include('myapp.urls')),             # Delegates app routes to myapp/urls.py
]