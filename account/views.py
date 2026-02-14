from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from account.forms import LoginForm, SignUpForm


def auth(request):
	signup_form = SignUpForm(prefix="signup")
	login_form = LoginForm(request=request, prefix="login")
	if request.method == "POST":
		action = request.POST.get("action")
		if action == "signup":
			signup_form = SignUpForm(request.POST, prefix="signup")
			if signup_form.is_valid():
				user = signup_form.save()
				login(request, user)
				return redirect("home")
		elif action == "login":
			login_form = LoginForm(request=request, data=request.POST, prefix="login")
			if login_form.is_valid():
				login(request, login_form.get_user())
				return redirect("home")

	return render(
		request,
		"account/auth.html",
		{"signup_form": signup_form, "login_form": login_form},
	)


def logout_view(request):
	if request.method == "POST":
		logout(request)
	return redirect("home")
