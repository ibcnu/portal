from django.urls import path, reverse_lazy
from apps.accounts.views import UserListView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


app_name = 'accounts'
urlpatterns = [
    path('user/', UserListView.as_view(), name='account_user'),

    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='account_login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('account_login')), name='account_logout'),


    path('password_change/',
         PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),
         name='account_password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='account_password_change_done'),

    path('password_reset/',
         PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
         name='account_password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='account_password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='account_password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='account_password_reset_complete'),

]
