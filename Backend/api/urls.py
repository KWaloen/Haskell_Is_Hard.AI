from django.urls import path
from .views import ai_response, conversation_history
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', ai_response, name="ai-response"),
    path('history/', conversation_history, name='conversation_history'),
]
