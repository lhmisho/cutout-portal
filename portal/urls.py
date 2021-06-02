from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.requirements_views import RequirementsListAPiView
from .views.addons_views import AddonsViewSet

router = DefaultRouter()

router.register('addons', AddonsViewSet)

urlpatterns = [
    path('requirements/', RequirementsListAPiView.as_view())
] + router.urls
