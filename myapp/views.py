from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.views import APIView
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import NoteModel

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World');


class NoteViews(APIView):

    #POST

    def post(self,request):
        print(request.data)
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #GET
    def get(self,request):

        NotesTable = NoteModel.objects.all()
        serializer = NoteSerializer(NotesTable,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #DELETE
    def delete(self,request):
        
        NotesTable = NoteModel.objects.all()
        NotesTable.delete()
        return Response({'message':'Data deleted successfully'},status=status.HTTP_200_OK)