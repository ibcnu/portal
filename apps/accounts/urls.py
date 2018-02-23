from django.urls import path, reverse_lazy
from apps.accounts.views import UserListView
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('user/', UserListView.as_view(), name='user'),

    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='accounts/logout'),


    path('password_change/',
         PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),
         name='accounts/password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='accounts/password_change_done'),

    path('password_reset/',
         PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
         name='accounts/password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='accounts/password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='accounts/password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='accounts/assword_reset_complete.html'),
         name='accounts/password_reset_complete'),

]
