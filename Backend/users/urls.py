"""Users URLs."""

from django.urls import path

from users import views

urlpatterns = [
    path('users/', views.UserApiViewset.as_view()),
    path('login/', views.LoginViewset.as_view()),
    path('logout/', views.LogoutViewset.as_view()),
    path('users/setpassword/', views.SettingPasswordView.as_view()),
    path('users/change-password/', views.ChangePasswordView.as_view()),
    path('users/add/', views.UsersAddFormData.as_view()),
    path('users/edit/<int:pk>/', views.UsersEditFormData.as_view()),
    path('users/delete/<int:pk>/', views.UsersDeleteFormData.as_view()),
    path('users/password_reset/', views.PasswordResetSendEmailView.as_view()),
    path('users/password_reset/confirm/',
         views.PasswordResetConfirmView.as_view()),
]
