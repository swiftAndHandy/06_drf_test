from django.db.migrations import serializer
from django.shortcuts import get_object_or_404
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from market_app.api.serializers import MarketSerializer, SellerSerializer, \
    ProductSerializer, SellerListSerializer
from market_app.models import Market, Seller, Product

# class MarketsView(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#
#     queryset = Market.objects.all()
#     serializer_class = MarketSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class SellerOfMarketList(generics.ListAPIView):
    serializer_class = SellerListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        market = get_object_or_404(Market, pk=pk)
        return market.sellers.all()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

# class SellerView(generics.ListAPIView):
#     serializer_class = SellerSerializer
#     queryset = Seller.objects.all()
#     class Meta:
#         model = Seller
#         fields = '__all__'
#
# class SellerViewDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SellerSerializer
#     queryset = Seller.objects.all()
#     class Meta:
#         model = Seller
#         fields = '__all__'