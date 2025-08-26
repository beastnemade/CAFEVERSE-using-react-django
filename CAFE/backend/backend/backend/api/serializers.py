from rest_framework import serializers
# from .models import MenuItem, Category, Table, Order, OrderItem
from .models import Menu,Item,MenuCategory,Dietary,Order
from accounts.serializers import UserSerializer


class DietarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dietary
        fields = ['name']

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['category']

class ItemSerializer(serializers.ModelSerializer):
    key = MenuCategorySerializer()
    dietary = DietarySerializer(many=True)
    class Meta:
        model = Item
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    key = MenuCategorySerializer()
    items = ItemSerializer(many=True)
    class Meta:
        model = Menu
        fields = ['id','key','name','items']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    order_items = ItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class MenuItemSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()

#     class Meta:
#         model = MenuItem
#         fields = '__all__'

# class OrderItemSerializer(serializers.ModelSerializer):
#     menu_item = MenuItemSerializer()

#     class Meta:
#         model = OrderItem
#         fields = '__all__'

# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True)

#     class Meta:
#         model = Order
#         fields = '__all__'