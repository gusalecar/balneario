from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset = User.objects.all(), lookup = 'iexact')]
    )
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
