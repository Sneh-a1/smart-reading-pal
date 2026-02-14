from django.urls import path

from account.views import auth, logout_view

urlpatterns = [
    path("account/", auth, name="auth"),
    path("account/logout/", logout_view, name="logout"),
]
