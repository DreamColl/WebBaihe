from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from baihe_api.apps.artical import views as artical_views
from baihe_api.apps.baihe_user import views as user_views

router = DefaultRouter()
router.register(r'articals', artical_views.ArticalViewSet)
router.register(r'users', user_views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token)
]
