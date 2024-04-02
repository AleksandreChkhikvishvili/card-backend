from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CardSerializer
from rest_framework import generics
from .models import Card

class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the card-collector api home route!'}
    return Response(content)

class CardList(generics.ListCreateAPIView):
  queryset = Card.objects.all()
  serializer_class = CardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Card.objects.all()
  serializer_class = CardSerializer
  lookup_field = 'id'