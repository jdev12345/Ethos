from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name = 'login'),
    path('homepage/',views.Home,name='Home'),
    path('signup/',views.sign_up,name='signUp'),
    path('convert/',views.askconvert,name='convert'),
    path('logout/',views.Logout,name='logout'),
    path('audio_detail/<pk>',views.audio_detail,name='aud_detail'),
    path('audioDelete/<pk>',views.delete_audio,name='del_audio'),
    path('deletecomment/<pk>',views.deletecomment,name='deleteComment'),
    path('download_view/',views.download_view,name='download_view'),
    path('analysis/<pk>',views.Analytics,name='analysis'),
    path('audio_analysis/<pk>',views.Analysis,name='analytic')
]