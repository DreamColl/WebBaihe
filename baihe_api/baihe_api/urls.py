from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from baihe_api.apps.artical import views as artical_views
from baihe_api.apps.baihe_user import views as user_views
from baihe_api.apps.form_builder import views as form_views
from baihe_api.apps.upload import views as upload_views

router = DefaultRouter()
router.register(r'articals', artical_views.ArticalViewSet)
router.register(r'form', form_views.BaiheFormViewSet)
router.register(r'form_data', form_views.BaiheFormDataViewSet)
router.register(r'users', user_views.UserViewSet)
router.register(r'upload/file', upload_views.FileViewSet)
router.register(r'upload/image', upload_views.ImageViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^token/', views.obtain_auth_token),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
