from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from NGO.models import foodAvbl, otherDetails
from Donate.models import FoodReq
from .serializer import AvblSerializer, ReqSerializer, DetailSerializer


class FoodAvailable(APIView):
    @staticmethod
    def get(request):
        list1 = foodAvbl.objects.all()
        serializer = AvblSerializer(list1, many=True)
        return Response(serializer.data)


class FoodRequest(APIView):
    @staticmethod
    def get(request):
        list1 = FoodReq.objects.all()
        serializer = ReqSerializer(list1, many=True)
        return Response(serializer.data)


class Details(APIView):
    @staticmethod
    def get(request):
        list1 = otherDetails.objects.all()
        serializer = DetailSerializer(list1, many=True)
        return Response(serializer.data)


def index(request):
    return render(request, "rest_api/api_home.html")

