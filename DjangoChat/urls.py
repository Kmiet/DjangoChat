from django.contrib import admin

from django.conf import settings

from django.conf.urls.static import static

from django.urls import path, include



from . import views



urlpatterns = [

    path('', views.index),

    path('login/', views.login_view),

    #path('register/', views.register),

    path('logout/', views.logout_handler),

    path('lobby/', include('lobby.urls')),

    path('admin/', admin.site.urls),

]



handler404 = 'DjangoChat.views.view_404'



if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)