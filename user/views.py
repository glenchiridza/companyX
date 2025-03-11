from django.db.models import Q
from django.shortcuts import reverse
from django.views import generic

from .forms import CustomUserCreationForm
from .models import User


class LandingPageView(generic.TemplateView):
    template_name = 'index.html'


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class UserServiceListView(generic.ListView):
    template_name = 'user/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        user = User.objects.filter(Q(is_staff=False) &
                                   Q(is_superuser=False) &
                                   Q(is_agent=False) &
                                   Q(is_customer=False))
        return user

class UserServiceDetailView(generic.DetailView):
    template_name = 'user/user_detail.html'
    context_object_name = 'user'

    def get_queryset(self):
        return User.objects.all()

