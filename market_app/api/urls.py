from django.urls import path, include

from market_app.api.views import \
    SellerOfMarketList, ProductViewSet, MarketViewSet, SellerViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('market', MarketViewSet)
router.register('seller', SellerViewSet)

app_name = 'market_api'

urlpatterns = [
    path('', include(router.urls)),
    path('market/<int:pk>/sellers/',SellerOfMarketList.as_view(), name='seller-market-detail'),
]