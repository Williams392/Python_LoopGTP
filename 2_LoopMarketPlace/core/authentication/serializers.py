from rest_framework import serializers  # 1

from .models import CustomUser  # 2

from django.core.validators import RegexValidator  # 3, YO


# Para la autenticación
class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=False, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    # phone_number = serializers.CharField(required=True)

    # Yo MEJORE, Personalizado:
    phone_number = serializers.CharField(
        required=True,
        validators=[
            RegexValidator(
                r'^\+\d{2}\s?\d{9}$',
                'Formato de número de teléfono no válido. '
                'Ejemplo: +51 999 999 999, debe ser de 9 digitos'
            )
        ]
    )

    class Meta:
        model = CustomUser
        fields = '__all__'

        # Cada uno, PERSONALIZADO mostrar:
        # fields = ('id', 'email', 'is_staff', 'password', 'first_name','last_name')


"""
_ Aviso REPASAR:

. `required`-> se utiliza para indicar si el campo es obligatorio (True) o no (False).
. `write_only` -> se utiliza para indicar que el campo solo debe ser utilizado para escribir datos.

_ RESUMEN:

. Este código define dos serializadores: `LoginSerializer`para la autenticación y `UserSerializer`
para la serialización de objetos CustomUser. Cada serializador tiene sus propios campos con 
diferentes requisitos y opciones de escritura.
"""
