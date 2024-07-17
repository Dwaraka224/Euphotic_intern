from django.shortcuts import render

# Create your views here.
#from rest_framework.views import APIView
from dishes.models import *
#from dishes.serializers import DishSerializer
#from rest_framework.response import Response


from dishes.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import APIView



class DishListView(APIView):
    def get(self,request):
        DO=Dishes.objects.all()
        DJO=DishSerializer(DO,many=True)
        return render(request,'dishlist.html',{'DO':DO})
    
    def post(self,request):
        DO=request.data
        DJO=DishSerializer(data=DO)
        if DJO.is_valid():
            DJO.save()
            return Response({"insert":"insert succsefully"})
        return Response({"Error":"Not inserted"})
    