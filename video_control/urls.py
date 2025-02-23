from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import ShowVideos, ShowPhotos, DetailPhoto, DetailVideo, Registration, Login, ProfileView, \
    UserPasswordChangeView, UpdateProfileView, RandomHomeList

urlpatterns = [
                  path('home/', RandomHomeList.as_view(), name='home'),
                  path('change_profile/<slug:slug>/', UpdateProfileView.as_view(), name='change_profile'),
                  path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
                  path('profile/<slug:slug>/', ProfileView.as_view(), name='profile'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('login/', Login.as_view(), name='login'),
                  path('register/', Registration.as_view(), name='register'),
                  path('video/', ShowVideos.as_view(), name='video_list'),
                  path('photo/', ShowPhotos.as_view(), name='photo_list'),
                  path('photo/<int:pk>/', DetailPhoto.as_view(), name='photo_detail'),
                  path('video/<int:pk>/', DetailVideo.as_view(), name='video_detail'),
                  # ]
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
