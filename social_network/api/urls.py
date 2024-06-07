from django.urls import path
from .views import LoginView, SignupView, UserSearchView, FriendRequestView, FriendListView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend-request/', FriendRequestView.as_view(), name='friend-request'),
    path('friends/', FriendListView.as_view(), name='friend-list'),
]