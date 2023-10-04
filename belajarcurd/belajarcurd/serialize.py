from rest_framework import serializers
from belajarcurd.models import Hero


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        # fields = ('id', 'name', 'hp', 'mana', 'job', 'speciality')
        fields = '__all__'  # klo mau semuanya
