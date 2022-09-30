from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ToDoSerializer
from .models import ToDo
# Create your views here.

class TodoView(APIView):
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer= ToDoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def get(self, request, *args, **kwargs):
        queryset = ToDo.objects.all()
        serializer = ToDoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def delete(self, request,pk, *args, **kwargs):
        obj = ToDo.objects.get(id=pk)
        if obj:
            obj.delete()
            return Response({"message":"todo deleted!!"}) 

    def put(self, request,pk, *args, **kwarg):
        obj = ToDo.objects.get(id=pk)
        data = request.data 
        serializer = ToDoSerializer(data=data, instance=obj)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

        
