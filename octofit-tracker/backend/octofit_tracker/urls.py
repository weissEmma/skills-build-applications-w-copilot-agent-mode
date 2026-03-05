
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet, api_root

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

def root_info(request):
    return HttpResponse('<h2>Welcome to Octofit Tracker API</h2><p>Use <a href="/api/">/api/</a> for API endpoints.</p>')

urlpatterns = [
    path('', root_info, name='root-info'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
