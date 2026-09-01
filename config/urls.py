from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from core.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Custom JWT Auth Endpoints (Inarudisha Token + User Role & School Data)
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # REST API Endpoints za Modules
    path('api/academics/', include('academics.urls')),
    path('api/students/', include('students.urls')),
]