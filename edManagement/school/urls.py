from django.urls import include, path, url
from rest_framework import routers
from school import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'siswa', SiswaViewSet)
# router.register(r'guru', SiswaViewSet)
# router.register(r'kelas', SiswaViewSet)

### Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('/admin/')
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   # url(r'^api/students/published$', views.tutorial_list_published)
]
