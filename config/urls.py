from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from core.views import CustomTokenObtainPairView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Session Auth kwa ajili ya Django REST Browsable API kwenye Browser
    path('api-auth/', include('rest_framework.urls')),

    # Custom JWT Auth Endpoints (Inarudisha Token + User Role & School Data)
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # REST API Endpoints za Modules
    path('api/academics/', include('academics.urls')),
    path('api/students/', include('students.urls')),
    path('api/finance/', include('finance.urls')),

    # API Documentation Endpoints (drf-spectacular)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]