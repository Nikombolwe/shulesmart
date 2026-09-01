from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import School, User

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'registration_number', 'subdomain', 'is_active']


class UserSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)
    role_display = serializers.CharField(source='get_role_display', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'role_display', 'school', 'phone_number']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Inaongeza data za mtumiaji na shule yake kwenye response ya Login API.
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Ongeza taarifa za user kwenye response JSON
        user_serializer = UserSerializer(self.user)
        data['user'] = user_serializer.data
        
        return data