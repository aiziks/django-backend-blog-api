
from django.contrib import admin
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from django.urls import path , include , re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('', include('blog.urls')),
    path('', include('account.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair' ) ,
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh' ),        
    
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #change this on production

