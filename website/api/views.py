from rest_framework.decorators import api_view
from rest_framework.response import Response
from website.api.serialzers import MessageSerializer
from website.models import Message

@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serialized_messages = MessageSerializer(messages, many=True)

    return Response(serialized_messages.data)

@api_view(['GET'])
def get_message(request, id):
    message = Message.objects.get(id=id)
    serialized_message = MessageSerializer(message, many=False)

    return Response(serialized_message.data)
