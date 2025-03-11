from django.urls import path

from market_app.api.views import sellers_view, product_view, sellers_single_view, \
    product_single_view, MarketsView, MarketDetailView, SellerOfMarketList

app_name = 'market_api'

urlpatterns = [
    path('market/', MarketsView.as_view(), name='markets'),
    path('market/<int:pk>/',MarketDetailView.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/',SellerOfMarketList.as_view(), name='seller-market-detail'),
    path('seller/', sellers_view),
    path('seller/<int:pk>/', sellers_single_view, name='seller-detail'),
    path('product/', product_view),
    path('product/<int:pk>/', product_single_view, name='product-detail')
]