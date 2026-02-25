from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Customers 
from .serializers import CustomerSerializer

# Create your views here.
 
class Customer(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
   
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class CustomerDetial(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def destroy(self, request, pk):
        return super().destroy(request, pk)
    