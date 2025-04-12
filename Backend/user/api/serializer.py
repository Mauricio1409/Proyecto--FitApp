from rest_framework.serializers import ModelSerializer
from user.models import User

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password']
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

    
class UserProfileUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'nivel_entrenamiento', 'objetivo', 'edad', 'peso', 'altura', 'foto_perfil']
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'nivel_entrenamiento', 'objetivo', 'edad', 'peso', 'altura', 'foto_perfil']
    