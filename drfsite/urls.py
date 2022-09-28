from django.urls import path, include, re_path

from drfsite.views import Listrest, CategoryList,Listrestdetail
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'data', Listrestdetail, basename='Products')
router.register(r'data', Listrest, basename='Products')
appname = 'drfsite'
urlpatterns = [
   path("v1/", include(router.urls)),
   path("v1/category/", CategoryList.as_view({'get': 'list'})),
   path("v1/two/", Listrest.as_view({'get': 'list'})),
   path('v1/drf_login/', include('rest_framework.urls')),
   path('v1/drf_auth/', include('djoser.urls')),
   re_path(r'^auth/', include('djoser.urls.authtoken')),
]

# from django.urls import path, include, re_path
#
# from drfsite.views import Listrest
# from rest_framework import routers
# router=routers.DefaultRouter()
# router.register(r'data',Listrest,basename='Products')
#
# appname='drfsite'
# urlpatterns=[
#    path("v1/",include(router.urls)),
#    path('v1/drf_login/',include('rest_framework.urls')),
#    path('v1/drf_auth/',include('djoser.urls')),
#    re_path(r'^auth/',include('djoser.urls.authtoken')),
# ]