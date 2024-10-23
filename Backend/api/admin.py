from django.contrib import admin
from .models import Conversation

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user_message', 'bot_response', 'timestamp')

admin.site.register(Conversation, ConversationAdmin)
