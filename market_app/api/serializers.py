from rest_framework import serializers
from market_app.models import Market, Seller, Products


class MarketSerializer(serializers.ModelSerializer):

    sellers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='seller_single')

    class Meta:
        model = Market
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets'
    )

    class Meta:
        model = Seller
        fields = '__all__'

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=100)
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    market = serializers.PrimaryKeyRelatedField(queryset=Market.objects.all())

    def create(self, validated_data):
        return Products.objects.create(**validated_data)
