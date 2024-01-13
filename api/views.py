from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from . import models 
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from rest_framework.response import Response
from django.shortcuts import redirect

def redirect_to_home(request):
    return redirect('home')

@api_view(["GET"])
def home(request):
    data = models.InvoiceDetail.objects.all()
    serializer = InvoiceDetailSerializer(data, many=True)    
    return Response(serializer.data)

class pk(generics.RetrieveUpdateAPIView):
    queryset=models.InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
    def get(self, request,pk, *args, **kwargs):
        data = models.InvoiceDetail.objects.filter(id=pk)
        serializer = InvoiceDetailSerializer(data, many=True)    
        return Response(serializer.data)
    
    def post(self, request,pk, *args, **kwargs):
        data = request.data
        invoice = models.Invoice(invoice=data['invoice']['invoice'],
        date=data['invoice']['date'],
        customer_name=data['invoice']['customer_name']
        )

        invoices = models.InvoiceDetail.objects.create(invoice=invoice,
        description=data['description'],
        quantity=data['quantity'],
        unit_price=data['unit_price'],
        price=data['price']
        )
         
        serializer =  InvoiceDetailSerializer(invoices,many=False)
        return Response(serializer.data)
        
        def put(self, request, pk, *args, **kwargs):
            data = request.data
            invoice_detail = get_object_or_404(models.InvoiceDetail, pk=pk)
            serializer = InvoiceDetailSerializer(invoice_detail, data=data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def patch(self, request, pk, *args, **kwargs):
            data = request.data
            invoice_detail = get_object_or_404(models.InvoiceDetail, pk=pk)

            serializer = InvoiceDetailSerializer(invoice_detail, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
