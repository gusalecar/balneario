from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset = get_user_model().objects.all(), lookup = 'iexact')]
    )
    password = serializers.CharField(write_only = True)

    class Meta:
        model = get_user_model()
        fields = '__all__'

    def create(self, validated_data):
        return get_user_model().objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
