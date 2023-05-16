from rest_framework import serializers  # 1

from .models import CustomUser  # 2


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserSerializer(serializers.ModelSerializer):

    # Omitiendo -> Para no mostrar:
    username = serializers.CharField(required=False, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = ('id', 'email', 'is_staff', 'password', 'first_name','last_name')
