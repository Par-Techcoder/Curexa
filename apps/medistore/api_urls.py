from apps.medistore import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path("medicines/", views.MedicineListAPIView.as_view(), name="medicine-list"),
    path('', include(router.urls)),
]
