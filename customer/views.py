from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Table,Category
from .serializers import CategoryWithItemsSerializer
from rest_framework.permissions import AllowAny


class MenuByTableView(APIView):
    permission_classes = [AllowAny]

    def get(self,request,token):

        table = get_object_or_404(Table,token=token,is_active=True)
    
        categories = Category.objects.all()

        serializer = CategoryWithItemsSerializer(categories,many=True)

        return Response({
            "table_number":table.number,
            "menu":serializer.data
        })


