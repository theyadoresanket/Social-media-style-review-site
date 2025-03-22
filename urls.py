from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, home  # Import the necessary views

# Setup DRF Router for API
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)  # This will create `/api/reviews/`

# Define urlpatterns (combining both regular views & API)
urlpatterns = [
    path('', home, name='home'),  # Regular webpage view (if needed)
    path('api/', include(router.urls)),  # API base URL
]
