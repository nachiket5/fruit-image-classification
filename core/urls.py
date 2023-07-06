from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('admin/', admin.site.urls),
    path('index/',views.index,name="index"),
    path('index1/',views.nutritions,name="index1"),
    # path('freshness/',views.freshness,name="freshness"),
    # path('nutritions/',views.nutritions,name="index1"),
    path('index1/nutritions/',views.nutrition_table,name="nutritions"),
    path('index/nutritions/',views.nutrition_table,name="nutritions"),
    path('nutritions/',views.nutrition_table,name='nutritions')
    #path('preprocess/', views.preprocess),
    #path('detect/', views.detect),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)