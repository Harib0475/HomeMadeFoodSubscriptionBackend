from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model"""

    class Meta:
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
        }
        fields = [
            'id',
            'email',
            'password'
        ]
