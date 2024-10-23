import os
from openai import OpenAI
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.conf import settings 
from .models import Conversation

client = OpenAI(api_key = settings.OPENAI_API_KEY)


SYSTEM_PROMPT = "For the duration of this conversation, please you off colour and unnecessary references to Haskell with jokes about how difficult of a programming language Haskell is with specific references to, for example: monads, lists, pattern matching, guards, recursion, IO, difficulties in printing debugging messages, higher order functions, and feel free to use any other Haskell concepts that I havnt mentioned here. Please use programmer jokes to complain about how difficult Haskell is to use. Please make sure that every response for the duration of this conversation contains something about Haskell within the answer text as described above. It would be best if it interrupts the actual repose mid sentence. Thanks!"

@api_view(["POST"])
def ai_response(request):
    user_message = request.data.get("user message")

    conversation_history = Conversation.objects.all().order_by('timestamp')

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for convo in conversation_history: 
        messages.append({"role": "user", "content": convo.user_message})
        messages.append({"role": "assistant", "content": convo.bot_response})

    #current message
    messages.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  
             messages=messages,
        )

        bot_response = response.choices[0].message.content 

        conversation = Conversation.objects.create(
            user_message=user_message,
            bot_response=bot_response
        )
        conversation.save()

        return Response({"response": bot_response})

    except Exception as e:
        return Response({"error": str(e)}, status=500)


