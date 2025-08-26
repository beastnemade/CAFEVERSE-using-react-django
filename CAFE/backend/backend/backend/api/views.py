from django.shortcuts import render,get_list_or_404
from django.http import JsonResponse

from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.response import Response
from .models import Menu,Item,Order
from accounts.models import User
from .serializers import MenuSerializer,OrderSerializer,ItemSerializer

class MenuView(APIView):
    # serializer_class = MenuSerializer
    # queryset = Menu.objects.all()
    permission_classes = [AllowAny]
    
    def get(self,request):
        data = Menu.objects.all()
        serializer = MenuSerializer(data , many=True)
        return Response({"data":serializer.data} )
    
class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        if request.user.role=='customer':    
            try:
                data = request.data
                item_list = Item.objects.filter(id__in = data.get('items',[]))
                user_data = Order.objects.create(user=User.objects.get(user = request.user))
                user_data.order_items.set(item_list)
                return Response({'status':'success'})
            except Exception as e:
                print(e)
                return Response({"status":"Failed"})
        else:
            return Response({"Error":"You can not forcefully enter any mislead data..."})
        
    def get(self,request):
        if request.user.role == 'customer':    
            try:
                orders = Order.objects.filter(user=request.user)
                serializer = OrderSerializer(orders,many=True)
                return Response({"data":serializer.data})
            except Exception as e:
                print(e)
                print(request.user)
                return Response({"status":"failed"})
        else:
            try:
                pending_orders = Order.objects.filter(status='pending').order_by('-date')
                completed_orders= Order.objects.filter(status='completed').order_by('date')
                pendings= OrderSerializer(pending_orders,many=True)
                completed= OrderSerializer(completed_orders,many=True)
                return Response({"pending":pendings.data,"completed":completed.data},status=200)
            except:
                return Response({"Error":"Unexpected Error generated.."})


class OrderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        if request.user.role != 'admin':
            return Response({"Error":"Only admins can update order status."})
        return super().update(request, *args, **kwargs)
    
class ItemDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def update(self,request,*args,**kwargs):
        if request.user.role != 'admin':
            return Response({"Error":"Only admins can update Items."})
        return super().update(request, *args, **kwargs)
    
    def delete(self,request, pk):
        if request.user.role != 'admin':
            return Response({"Error":"Only admins can delete Items."})
        try:
            order = self.get_object()
            order.delete()
            return Response({"message": "Order deleted successfully."})
        except Order.DoesNotExist:
            return Response({"error": "Order not found."},status=404)