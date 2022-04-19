from rest_framework          import status
from rest_framework.views    import APIView
from rest_framework.response import Response

from django.db.models import Q, Count, F

from .models      import Product
from .serializers import ProductsSerializer

class ProductsListView(APIView):
    def post(self, request):
        data = request.data
        serializer = ProductsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        search = request.GET.get("search", None)
        order_by = request.GET.get("order_by", "생성일")

        q = Q()

        if search:
            q &= Q(title__icontains = search)

        order_list = {"생성일":"-created_at", "총펀딩금액":"-sum_price"}

        products = (Product.objects
            .filter(q)
            .annotate(sum_price = Count('pd_fund') * F('one_price'))
            .order_by(order_list[order_by])
            )
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

class ProductsDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    def patch(self, request, pk):
        data = request.data
        product = Product.objects.get(pk=pk)
        serializer = ProductsSerializer(product, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)