from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import (LoginView, LogoutView,PasswordResetView,PasswordResetDoneView,
                                       PasswordResetConfirmView,PasswordResetCompleteView,PasswordChangeView,PasswordChangeDoneView)
from django.urls import path, include


from user.views import LandingPageView

urlpatterns = [
       path('', LandingPageView.as_view(), name='landing_page'),
       path('admin/', admin.site.urls),
       path('users/', include('user.urls', namespace='users')),
       path('login/', LoginView.as_view(), name='login'),
       path('logout/', LogoutView.as_view(), name='logout'),
       path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
       path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
       path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
       path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
       path('password-change/', PasswordChangeView.as_view(), name='password_change'),
       path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
