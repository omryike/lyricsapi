from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('artists',views.ArtistView)
router.register('songs',views.SongView)

urlpatterns = [
    path('',include(router.urls))
]