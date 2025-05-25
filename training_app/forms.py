from django import forms
<<<<<<< HEAD

class PromptForm(forms.Form):
    prompt = forms.CharField(label="enter your prompt:", max_length=500)
=======
from django.contrib.auth.forms import UserCreationForm
from training_app.models import User

class PromptForm(forms.Form):

    prompt = forms.CharField(label="enter your prompt:", max_length=500, widget=forms.Textarea)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
>>>>>>> feature/adding_bulma
