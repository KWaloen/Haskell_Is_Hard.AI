from django.urls import path
from .views import ai_response
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('haskellishardchat/', ai_response, name="ai-response")
]
