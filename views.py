from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
def home(request):
    return render(request, 'reviews/home.html')
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')  # Get latest reviews first
    serializer_class = ReviewSerializer
