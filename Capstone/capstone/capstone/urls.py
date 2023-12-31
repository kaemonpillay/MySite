from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('about_us/', include('about_us.urls')),
    path('login/', user_views.login, name='login'),
]