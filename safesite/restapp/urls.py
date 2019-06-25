from django.urls import path

from .views import GroupView
from .views import UserView


app_name = "restapp"


urlpatterns = [
    path('groups/', GroupView.as_view()),
    path('groups/<int:pk>', GroupView.as_view()),
    path('user/', UserView.as_view()),
    path('user/<int:pk>', UserView.as_view()),
]
