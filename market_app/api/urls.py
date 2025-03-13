from django.urls import path, include

from market_app.api.views import sellers_view, sellers_single_view, \
    SellerOfMarketList, ProductViewSet, MarketViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register('product', ProductViewSet)
router.register('market', MarketViewSet)

app_name = 'market_api'

urlpatterns = [
    path('', include(router.urls)),

    path('market/<int:pk>/sellers/',SellerOfMarketList.as_view(), name='seller-market-detail'),
    path('seller/', sellers_view),
    path('seller/<int:pk>/', sellers_single_view, name='seller-detail'),
]