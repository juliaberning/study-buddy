from django.forms import ModelForm
from .models import Message, Room, User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email']