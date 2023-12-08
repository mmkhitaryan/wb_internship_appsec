# myapp/views.py
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import BoardPost

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class BoardPostsListView(ListView):
    model = BoardPost
    paginate_by = 100

class BoardPostsCreateView(LoginRequiredMixin, CreateView):
    model = BoardPost
    fields = ["image", "content"]
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        # Set the owner of the model instance to the current user
        form.instance.owner = self.request.user
        return super().form_valid(form)

