from rest_framework import serializers
from market_app.models import Market, Seller, Product


class MarketSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='market_api:market-detail', lookup_field='pk'
    )

    sellers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='market_api:seller-detail')

    class Meta:
        model = Market
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets',
    )

    class Meta:
        model = Seller
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # seller = SellerSerializer(many=False, read_only=True)

    market_id = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        source='market',
        write_only=True,
        required=True
    )

    seller_id = serializers.PrimaryKeyRelatedField(
        queryset=Seller.objects.all(),
        source='seller',
        write_only=True,
        required=True
    )

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1
