from django.contrib import admin
from django.urls import path, include
from notes.views import register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # MAIN APP
    path('notes/', include('notes.urls')),

    # AUTH
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # DEFAULT REDIRECT
    path('', include('notes.urls')),  # IMPORTANT LINE
]