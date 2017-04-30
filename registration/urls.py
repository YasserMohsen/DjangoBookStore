from django.conf.urls import url
from registration import views as reg_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            redirect_authenticated_user='library/'),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(),
        name='logout'),
    url(r'^signup/$',reg_views.Signup.as_view()),
]