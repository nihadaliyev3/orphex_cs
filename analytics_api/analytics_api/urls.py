from django.urls import path, include

urlpatterns = [
    # Include the analytics app's URLs
    path('api/', include('analytics.urls')),  # Add this line
]
