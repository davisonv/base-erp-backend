from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioCreateSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)
    
    class Meta:
        model = get_user_model()
        fields = 'id', 'username', 'first_name', 'last_name', 'email', 'password', 'funcao',
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UsuarioCreateSerializer, self).create(validated_data)
    

class UsuarioUpdateGetSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = 'id', 'username', 'first_name', 'last_name', 'email', 'funcao', 'is_active',
        

class UsuarioUpdateSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)
    
    class Meta:
        model = get_user_model()
        fields = 'password',
    
    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        instance.password = validated_data['password']
        return instance


class UsuarioListSerializer(ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # retorno padrão da classe pai
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # novos campos
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        data.update({'funcao': self.user.funcao})
        
        return data