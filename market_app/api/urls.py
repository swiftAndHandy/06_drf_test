from django.urls import path

from market_app.api.views import markets_view, markets_single_view, sellers_view, product_view, sellers_single_view

app_name = 'market_api'

urlpatterns = [
    path('market/', markets_view),
    path('market/<int:pk>/', markets_single_view),
    path('seller/', sellers_view),
    path('seller/<int:pk>/', sellers_single_view, name='seller_single'),
    path('product/', product_view)
]