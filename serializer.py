from rest_framework import serializers
from country.models import Country
from django.contrib.auth.models import User


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta :
        model = Country
        fields = ['url', 'id', 'name', 'government_type', 'important_sports',  'owner', 'products', ]



class UserSerializer(serializers.ModelSerializer):
    country = serializers.HyperlinkedRelatedField(many=True, view_name='country-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'country']
