from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'areas-pesquisa', AreaPesquisaViewSet)
router.register(r'projetos', ProjetoViewSet)
router.register(r'publicacoes', PublicacaoViewSet)
router.register(r'orientacoes', OrientacaoViewSet)
router.register(r'contato', ContatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
