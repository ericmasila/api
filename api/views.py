from django.http import JsonResponse

import api
from .models import Api
from .serializers import ApiSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def api_list(request, format=None):
    if request.method == 'GET':
        api = Api.objects.all()
        serializer = ApiSerializer(api, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, id):
    try:
        Api.objects.get(pk=id)
    except Api.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApiSerializer(api)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApiSerializer(api, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        api.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)