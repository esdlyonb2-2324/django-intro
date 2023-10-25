from django.forms import ModelForm, Textarea

from website.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content']
        widgets = {
            "content" : Textarea(attrs={"cols": 20, "rows": 4})

        }
