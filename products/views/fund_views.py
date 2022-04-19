from rest_framework          import status
from rest_framework.views    import APIView
from rest_framework.response import Response

from ..models      import Pd_Fund
from ..serializers import Pd_FundSerializer


class Pd_FundView(APIView):
    def post(self, request):
        data = request.data
        serializer = Pd_FundSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = Pd_Fund.objects.all()
        serializer = Pd_FundSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)