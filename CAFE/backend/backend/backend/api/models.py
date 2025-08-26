from django.db import models
from accounts import models as AccountModels
# Create your models here.

class Dietary(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class MenuCategory(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField()
    popular = models.BooleanField(default=False)
    seasonal = models.BooleanField(default=False)
    calories = models.IntegerField()
    dietary = models.ManyToManyField(Dietary)
    key = models.ForeignKey(MenuCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Menu(models.Model):
    key = models.ForeignKey(MenuCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f' {self.key} / ({self.name})'

class Order(models.Model):
    status_choice = (
        ('pending',"Pending"),
        ('completed',"Completed"),
    )
    user = models.ForeignKey(AccountModels.User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    order_items = models.ManyToManyField(Item)
    status = models.CharField(max_length=20,choices=status_choice,default='pending')

# class Category(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


# class MenuItem(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField(upload_to='menu/', null=True, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
#     is_available = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name


# class Table(models.Model):
#     number = models.PositiveIntegerField(unique=True)

#     def __str__(self):
#         return f"Table {self.number}"


# class Order(models.Model):
#     table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     is_completed = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Order {self.id}"


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} x {self.menu_item.name}"