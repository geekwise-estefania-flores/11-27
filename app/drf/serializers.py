from django.contrib.auth.models import User, Group
from rest_framework import serializers 
	
class User_Serializers( serializers.HyperlinkedModelSerializer ):
	class Meta:
		model = User 
		fields = [
			'Url',
            'Username',
            'Email'
            'Groups',
        ]

class Group_Serializers(serializers.HyperlinkedModelSerializer ):   
	class Meta:
		model = Group 
		fields = [
            'Username',
            'Email'
        ]