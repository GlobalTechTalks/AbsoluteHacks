from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("AbsoluteHackInit.urls")),
    path('accounts/', include("accounts.urls")),
]
