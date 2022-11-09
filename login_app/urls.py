from django.urls import path
from login_app import views

app_name = "login_app"


urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login, name="login"),
    path('edit/', views.edit_profile, name="edit"),
    path('logout/', views.logout_user, name="logout")
]
