"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator
from core.utils import ChoiceDisplayField
# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from users.models import UserProfile
from .models import TYPE_USER


class UserModelSerializer(serializers.ModelSerializer):

    type_user = ChoiceDisplayField(TYPE_USER)

    class Meta:
        model = UserProfile
        exclude = ['password', 'is_staff', 'modified_date', 'created_date',
                   'user_permissions', 'date_joined', ]
        depth = 1


class UserModelHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        # fields = "__all__"
        fields = ['username', 'email']
        # depth = 1


class UserHistorySerializer(serializers.ModelSerializer):

    history_user = UserModelHistorySerializer()

    class Meta:
        model = UserProfile.history.model
        fields = ('id', 'username', 'history_id', 'history_type',
                  'history_date', 'history_change_reason', 'history_user')
        depth = 1


class UserLoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el
        # objeto del usuario
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Credentials are not valid.')

        # Guardamos el usuario en el contexto para posteriormente en create
        # recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserRegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=UserProfile.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=UserProfile.objects.all())]
    )

    address = serializers.CharField(max_length=250, allow_null=True,
                                    allow_blank=True)

    zip_code = serializers.CharField(max_length=10, allow_null=True,
                                     allow_blank=True)

    birth_date = serializers.DateField(required=False, allow_null=True,)

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message=f"Debes introducir un número con el siguiente formato: "
                f"+999999999. El límite son de 15 dígitos."
    )

    phone_number = serializers.CharField(validators=[phone_regex],
                                         allow_null=True, allow_blank=True)

    timezone = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)

    type_user = serializers.CharField(max_length=15, allow_null=True, allow_blank=True)

    status = serializers.BooleanField(allow_null=True)

    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)

    def create(self, data):
        # data.pop('password_confirmation')
        user = UserProfile.objects.create_user(**data)
        return user

