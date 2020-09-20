from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset = User.objects.all(), lookup = 'iexact')]
    )

    class Meta:
        model = User
        fields = '__all__'
