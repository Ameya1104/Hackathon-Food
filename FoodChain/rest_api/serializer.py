from rest_framework import serializers
from NGO.models import foodAvbl, otherDetails
from Donate.models import FoodReq


class AvblSerializer(serializers.ModelSerializer):
    class Meta:
        model = foodAvbl
        fields = ('id', 'quantity', 'Other_Specifics', 'city', 'pickup_address', 'created_on', 'edible', 'user', 'measurement')


class ReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodReq
        fields = ['id', 'foodtakenfrom', 'quantity_required', 'user']


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = otherDetails
        fields = ('id', 'address', 'phonenumber', 'user', 'city')
