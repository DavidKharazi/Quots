from django.urls import path
from .views import RandomQuotesViewSet

urlpatterns = [
    path('random_user/', RandomQuotesViewSet.as_view(), name='random_user'),
]