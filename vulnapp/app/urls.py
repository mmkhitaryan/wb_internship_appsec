from django.urls import path
from .views import RegisterView, LoginView, BoardPostsListView, BoardPostsCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', BoardPostsListView.as_view(), name='main'),
    path('create/', BoardPostsCreateView.as_view(), name='message-post'),
]
