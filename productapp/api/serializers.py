from category.models import Category
from productapp.models import Product
from rest_framework import serializers
from productapp.models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), allow_null=True, required=False)
    # image = serializers.ImageField(upload_to='productapp/images')

    def create(self, validated_data):

        return Product.objects.create(**validated_data)

    # ====================================

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

#==========================================================================


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['id','name']


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer(read_only=True)
    cat_name = serializers.StringRelatedField(source='category.name')
    category_id = serializers.StringRelatedField(source='category.id')
    # cat_id = serializers.IntegerField(source='category.id')
    # cat_id = serializers.IntegerField(source='category')

    class Meta:
        model = Product
        fields = '__all__'
        fields.__add__('cat_name')
        fields.__add__('category_id')
