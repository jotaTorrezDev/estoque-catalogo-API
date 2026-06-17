from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'produtos', views.ProdutoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'pedidos', views.PedidosViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token),
    path('pedidos/', views.PedidosViewSet.as_view({'get': 'list', 'post': 'create'}), name='pedidos-list'),
    
]