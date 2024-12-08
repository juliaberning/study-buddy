from django.forms import ModelForm
from .models import Message, Room

class RoomForm(ModelForm):
    class Meta: 
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        #fields = ['name', 'topic']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']