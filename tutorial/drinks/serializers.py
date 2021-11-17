from rest_framework import serializers
from drinks.models import Drink

"""
class DrinkSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)

    def create(self, validated_data):

        return Drink.objects.create(**validated_data)


    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        return instance
"""

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['name', 'description']