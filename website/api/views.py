from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from website.api.serializers import MessageSerializer
from website.models import Message, User, Category


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request):
    messages = Message.objects.all()
    serialized_messages = MessageSerializer(messages, many=True)

    #return Response(request.user.username)
    return Response(serialized_messages.data)

@api_view(['GET'])
def get_message(request, id):
    message = Message.objects.get(id=id)
    serialized_message = MessageSerializer(message, many=False)

    return Response(serialized_message.data)

@api_view(['POST'])
def new_message(request):
    if request.method == 'POST':
        newMessage = Message()
        newMessage.author = User.objects.get(id=1)
        message = MessageSerializer(instance=newMessage, data=request.data)
        if message.is_valid():
            message.save()
            return Response(message.data)
    return None