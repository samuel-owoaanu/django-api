from typing import List
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import LinkSerializer
from .models import Link
# Create your views here.

class LinkListView(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class LinkCreateView(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkDetailView(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkUpdateView(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkDeleteView(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

