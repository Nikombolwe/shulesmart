from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom Login Endpoint inayotumia Custom Serializer yetu.
    """
    serializer_class = CustomTokenObtainPairSerializer