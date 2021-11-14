from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializer


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerilizer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'USer HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"""Hello {name}"""
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response(
            {'method':'PUT'}
        )

    def patch(self, request, pk=None):
        """Handle partial update an object"""

        return Response(
            {'method':'PATCH'}
        )

    def delete(self, request, pk=None):
        """Handle deleting an object"""

        return Response(
            {'method':'DELETE'}
        )