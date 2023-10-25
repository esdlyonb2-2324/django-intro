from django.forms import ModelForm, Textarea

from website.models import Message, User


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content']
        widgets = {
            "content" : Textarea(attrs={"cols": 20, "rows": 4})

        }

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
