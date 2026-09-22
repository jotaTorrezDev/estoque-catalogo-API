from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'produtos', views.ProdutoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'pedidos', views.PedidosViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token),
    path('pedidos/', views.PedidosViewSet.as_view({'get': 'list', 'post': 'create'}), name='pedidos-list'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
