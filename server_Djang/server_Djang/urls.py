
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from welcomeApp.views import initPage, aboutPage
from twoapp.views import buildPage, CurrentBuild
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initPage),
    path('about/', aboutPage, name="about_path" ),
    path('buildings/', buildPage, name = "buildscan"),
    path('build/', CurrentBuild, name = "current")
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)