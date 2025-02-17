from rest_framework import serializers
from market_app.models import Market, Seller, Products


class MarketSerializer(serializers.Serializer):
    class Meta:
        model = Market
        fields = '__all__'

class SellerDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    contact_info = serializers.CharField()
    markets = MarketSerializer(read_only=True, many=True)

class SellerCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    contact_info = serializers.CharField()
    markets = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    def validate_markets(self, value):
        markets = Market.objects.filter(id__in=value)
        if  markets.count() != len(value):
            raise serializers.ValidationError("Market IDs do not match")
        return value

    def create(self, validated_data):
        market_ids = validated_data.pop('markets')
        seller = Seller.objects.create(**validated_data)
        seller.markets.set(market_ids)
        return seller

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=100)
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    market = serializers.PrimaryKeyRelatedField(queryset=Market.objects.all())

    def create(self, validated_data):
        return Products.objects.create(**validated_data)
