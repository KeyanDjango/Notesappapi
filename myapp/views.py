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


class NoteDeleteOne(APIView):

    #Delete One

    def delete(self,request,id):

        try:
            NoteTable = NoteModel.objects.get(id=id)
            NoteTable.delete()
            return Response({'message':'Data deleted successfully'},status=status.HTTP_200_OK)
        except NoteModel.DoesNotExist:
            return Response({'message':'Data id is not found'},status=status.HTTP_400_BAD_REQUEST)

class NoteUpdateOne(APIView):

    #Update One

    def put(self,request,id):
        try:
            
            tablenote = NoteModel.objects.get(id=id)
            serializer = NoteSerializer(tablenote,data=request.data)
        
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except NoteModel.DoesNotExist:
            return Response({'message','Data id is not found'},status=status.HTTP_400_BAD_REQUEST)
