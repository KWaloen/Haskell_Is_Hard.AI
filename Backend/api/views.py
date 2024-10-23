import os
from openai import OpenAI
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.conf import settings 

client = OpenAI(api_key = settings.OPENAI_API_KEY)


SYSTEM_PROMPT = "For the duration of this conversation, please you off colour and unnecessary references to Haskell with jokes about how difficult of a programming language Haskell is with specific references to, for example: monads, lists, pattern matching, guards, recursion, IO, difficulties in printing debugging messages, higher order functions, and feel free to use any other Haskell concepts that I havnt mentioned here. Please use programmer jokes to complain about how difficult Haskell is to use. Please make sure that every response for the duration of this conversation contains something about Haskell within the answer text as described above. It would be best if it interrupts the actual repose mid sentence. Thanks!"

@api_view(["POST"])
def ai_response(request):
    user_message = request.data.get("user message")
   
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  
             messages=[
                {"role": "system", "content": SYSTEM_PROMPT},  # System prompt defines the behavior
                {"role": "user", "content": user_message},     # User's prompt
            ]
        )
        return Response({"response": response.choices[0].message.content})

    except Exception as e:
        return Response({"error": str(e)}, status=500)