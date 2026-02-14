


from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from account.models import User


class SignUpForm(UserCreationForm):
	email = forms.EmailField(required=True)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.setdefault("class", "w-full border border-black px-3 py-2")

	class Meta:
		model = User
		fields = ("email", "name", "city", "password1", "password2")


class LoginForm(AuthenticationForm):
	username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"autofocus": True}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs.setdefault("class", "w-full border border-black px-3 py-2")



