from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = User
        fields = ('id', 'email', 'first_name', 
                    'last_name', 'avatar', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        email = data.pop('email')
        password = data.pop('password')

        return User.objects.create_user(email, password, **data)