from rest_framework.response import Response
from rest_framework.decorators import api_view
from website.api.serialzers import MessageSerializer
from website.models import Message

@api_view(['GET'])

def get_messages(request):
    messages = Message.objects.all()
    serialized_messages = MessageSerializer(messages, many=True)

    return Response(serialized_messages.data)


def get_message(request):
    return None