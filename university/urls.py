from django.urls import path
from university import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', views.UniverListView.as_view(), name = "uni"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    