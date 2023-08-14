from rest_framework.decorators import api_view
from .models import Dpd, Dpp
from .serializers import DpdSerializer, DppSerializer
from rest_framework.response import Response
from rest_framework import viewsets

@api_view(['GET'])
def dpd_list(request):
    posts = Dpd.objects.all()
    serializer = DpdSerializer(posts, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def dpp_list(request):
    posts = Dpp.objects.all()
    serializer = DppSerializer(posts, many=True)
    return Response(serializer.data)