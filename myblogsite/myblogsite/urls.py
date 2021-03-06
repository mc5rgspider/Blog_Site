
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.all_blogs, name='all_blogs'),
    path('', include('blog.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
