from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import *
from products.serializers import ProductSerializers

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    
    
    
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializers(instance).data
    return Response(data)