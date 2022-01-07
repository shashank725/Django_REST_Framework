from django.db.models import fields
from rest_framework import serializers, validators
from .models import Student

# Model Serializer
class StudentSerializer(serializers.ModelSerializer):
# Validators
    def starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with R')

    # name = serializers.CharField(read_only=True)
    name = serializers.CharField(validators=[starts_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']
        extra_kwargs = {'name':{'read_only':True}}

# Field Level Validation
    def validated_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

# Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data