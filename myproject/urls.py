from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name='base'),
    path('home/', home, name='home'),
    path('search/', search, name='search'),


    path('profile/', profile, name='profile'),
    path('update_profile/<int:id>', update_profile, name='update_profile'),


    path('addform/', addform, name='addform'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('trainers/', trainers, name='trainers'),
    path('starter_page/', starter_page, name='starter_page'),
    path('pricing/', pricing, name='pricing'),
    path('events/', events, name='events'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),



    path('video_courses/<int:id>', video_courses, name='video_courses'),
    path('auther/<int:id>', auther, name='auther'),
    path('singleauther/<int:id>', singleauther, name='singleauther'),
    path('courses/', courses, name='courses'),
    path('course_details/<int:id>', course_details, name='course_details'),


    path('', loginpage, name='loginpage'),
    path('logoutpage/', logoutpage, name='logoutpage'),
    path('registerpage/', registerpage, name='registerpage'),
    path('password_change/', password_change, name='password_change'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
