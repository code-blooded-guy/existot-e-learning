from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'username', )

class SignUpSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = models.User
        fields = ('email', 'username', 'password1' ,'password2' )

    def validate(self, data):
        """
        Check that start is before finish.
        """
        print('password1' not in data or 'password2' not in data)
        if 'password1' not in data or 'password2' not in data:
            raise serializers.ValidationError("plz enter password")

        if data['password1'] != data['password2']:
            raise serializers.ValidationError("password not match")
        print(data)
        return data