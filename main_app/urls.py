from django.urls import path
from .views import Home, CardList, CardDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('card/', CardList.as_view(), name='card-list'),
  path('card/<int:id>/', CardDetail.as_view(), name='card-detail'),
]
