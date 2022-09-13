from rest_framework import serializers
from .models import CustomUser, Organization, Donations


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')


class DonationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = ('donor', 'donation_amount')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('representative',
                  'name',
                  'country',
                  'contact',
                  'license_verification')
