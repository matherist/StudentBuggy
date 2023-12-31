from django.contrib import admin
from django.urls import path,include
from users import views as dash_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('allauth.urls')),
    path('', include('users.urls')),
    path('register/', dash_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="dashboard/login.html"), name="login"),
    path('profile/', dash_views.profile, name='profile'),
    path('logout/',  auth_views.LogoutView.as_view(template_name="dashboard/logout.html"), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)