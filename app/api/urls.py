from django.urls import include, path
from rest_framework import routers
from api.notes.views import NoteViewSet
#from api.users.views import UserLoginView


app_name = "api"

router = routers.DefaultRouter()
router.register(r"notes", NoteViewSet, basename="notes")


urlpatterns = [
    path("", include(router.urls)),
    # path("login/", UserLoginView.as_view(), name="login"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]
