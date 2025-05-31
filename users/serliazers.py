from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from .models import Group

User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        token['mobile_number'] = user.mobile_number
        token['role'] = user.role.name if user.role else None
        return token

class UserProfileSerializer(serializers.ModelSerializer):
    role = GroupSerializer(read_only=True)
    password = serializers.CharField(write_only=True, required=False)
    joining_date = serializers.DateField(required=True)
    bank_account = serializers.JSONField(required=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'mobile_number', 'email', 'joining_date', 
                 'salary', 'address', 'dob', 'role', 'documents', 'bank_account',
                 'emergency_contact', 'profile_image', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
        else:
            # Set default password as first 4 chars of name + last 4 digits of mobile
            default_password = f"{validated_data['full_name'][:4].lower()}{validated_data['mobile_number'][-4:]}"
            user.set_password(default_password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        mobile_number = data.get('mobile_number')
        email = data.get('email')
        password = data.get('password')

        if not mobile_number and not email:
            raise serializers.ValidationError("Either mobile number or email is required.")

        user = None
        if mobile_number:
            try:
                user = User.objects.get(mobile_number=mobile_number)
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid mobile number.")
        elif email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid email.")

        if user and not user.check_password(password):
            raise serializers.ValidationError("Invalid password.")

        return data

class ForgotPasswordSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    def validate(self, data):
        mobile_number = data.get('mobile_number')
        email = data.get('email')

        if not mobile_number and not email:
            raise serializers.ValidationError("Either mobile number or email is required.")

        return data

