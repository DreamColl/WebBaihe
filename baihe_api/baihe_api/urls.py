from django.conf.urls import include, url
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from baihe_api.apps.artical import views as artical_views
from baihe_api.apps.baihe_user import views as user_views
from baihe_api.apps.form_builder import views as form_views

router = DefaultRouter()
router.register(r'articals', artical_views.ArticalViewSet)
router.register(r'form', form_views.BaiheFormViewSet)
router.register(r'form_data', form_views.BaiheFormDataViewSet)
router.register(r'users', user_views.UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^token/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
