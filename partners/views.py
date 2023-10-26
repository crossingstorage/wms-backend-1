from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Customer, Consignee, Carrier, CarrierAddress, Contact, Bank
from .serializers import (
    CustomerSerializer,
    ConsigneeSerializer,
)


class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConsigneeList(APIView):
    def get(self, request):
        consignees = Consignee.objects.all()
        serializer = ConsigneeSerializer(consignees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConsigneeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsigneeDetail(APIView):
    def get_object(self, pk):
        try:
            return Consignee.objects.get(pk=pk)
        except Consignee.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        consignee = self.get_object(pk)
        serializer = ConsigneeSerializer(consignee)
        return Response(serializer.data)

    def put(self, request, pk):
        consignee = self.get_object(pk)
        serializer = ConsigneeSerializer(consignee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        consignee = self.get_object(pk)
        consignee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
