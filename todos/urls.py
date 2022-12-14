from rest_framework import routers
from .api import TodoViewSet, DeleteAllTodo, GetAllTodo
#Taller vistas
from django.urls import path
#Taller JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView





router = routers.DefaultRouter()

router.register('api/v1/todo', TodoViewSet, 'todos')


urlpatterns = [
    path('api/v1/todo/delAll', DeleteAllTodo.as_view(),name='delAll'),  #Para este caso estamos agregándolo como un as_view() debido a que necesitamos retornar una vista que pueda hacer uso de un request y haga un response.
    path('api/v1/todo/getAll', GetAllTodo.as_view(),name='getAllTodo'),

    #parte de la librería de SimpleSWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls   #para concatenar las URLS


