from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from market_app.api.serializers import MarketSerializer, SellerSerializer, \
    ProductSerializer
from market_app.models import Market, Seller, Products


@api_view(['GET', 'POST'])
def markets_view(request):
    if request.method == 'GET':
        markets = Market.objects.all()
        serializer = MarketSerializer(markets, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def markets_single_view(request, pk):
    market = get_object_or_404(Market, pk=pk)

    if request.method == 'GET':
        serializer = MarketSerializer(market)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MarketSerializer(market, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        market.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def sellers_view(request):
    if request.method == 'GET':
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def sellers_single_view(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    if request.method == 'GET':
        serializer = SellerSerializer(seller)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SellerSerializer(seller, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)