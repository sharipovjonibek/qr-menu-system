from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({
            "id":request.user.id,
            "username":request.user.username,
            "role":request.user.role
        })