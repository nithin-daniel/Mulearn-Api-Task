from django.shortcuts import render,redirect,HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import Login
from rest_framework import status
from rest_framework.decorators import action
# Create your views here.
# class LoginPage(viewsets.ViewSet):
#     def create(self,request):
#         results = Login( many=True).data
#         return Response(results)




class LoginPage(viewsets.ModelViewSet):
    serializer_class = Login
    @action(detail=False, methods=['GET', 'POST'])
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            serializer = Login(data=request.data)
            if serializer.is_valid():
                if serializer.validated_data['name'] == 'aswin' and serializer.validated_data['password'] == '1234':
                    return Response(status=status.HTTP_200_OK)
            else:
                return HttpResponse('Not User')
            # print(serializer)
        return Response({})
