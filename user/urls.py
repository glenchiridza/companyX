from django.urls import path

from user.views import SignUpView,UserServiceListView,UserServiceDetailView

app_name = 'user'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('<int:pk>/', UserServiceDetailView.as_view(), name='user_detail'),
    path('list/', UserServiceListView.as_view(), name='user_list'),
    
]