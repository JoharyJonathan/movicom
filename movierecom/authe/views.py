from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def Test(request):
    data = {
        'Test': 'Mandeha ve le izy',
        'Message': 'status 200',
        'code': 201,
    }
    return Response(data)