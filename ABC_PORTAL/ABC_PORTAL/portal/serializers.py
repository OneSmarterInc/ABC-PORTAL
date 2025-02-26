# serializers.py
from rest_framework import serializers
from .models import MyappElghp,MyappEmpyp,MyappDepnp,MyappRecentData,MyappMssqlCountModel
from django.contrib.auth.models import User
import re


# Serializer for user signup (creating a new user)
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate_username(self, value):
        # Ensure the username only contains letters
        if not re.match(r'^[a-zA-Z]+$', value):
            raise serializers.ValidationError("Username should only contain letters.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    
class OTPLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=True)  
    otp = serializers.CharField(max_length=6, required=True)    
          

class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyappMssqlCountModel
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    EDOB = serializers.SerializerMethodField()
    elghp_data = serializers.SerializerMethodField()  

    class Meta:
        model = MyappEmpyp
        fields = ['EMMEM', 'EMNAME', 'EMJOB', 'EMSSN', 'EDOB', 'elghp_data']

    def get_EDOB(self, obj):
        """Format DOB as DD/MM/YYYY."""
        if obj.EMDOBY and obj.EMDOBM and obj.EMDOBD:
            return f"{obj.EMDOBM:02d}/{obj.EMDOBD:02d}/{obj.EMDOBY:04d}"
        return None  

    def get_elghp_data(self, obj):
        """Fetch ELPLAN, ELCLAS, ELTYP from elghp based on matching EMSSN."""
        try:
            related_record = MyappElghp.objects.get(ELSSN=obj.EMSSN)  # Match using EMSSN
            return {
                "ELPLAN": related_record.ELPLAN,
                "ELCLAS": related_record.ELCLAS,
                "ELTYP": related_record.ELTYP,
            }
        except MyappElghp.DoesNotExist:
            return None  
        
class MyappRecentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyappRecentData
        fields = '__all__'


class EmpypSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyappEmpyp
        fields = ["id","emclnt","emssn","emmem","emadr1","emcity","emname","emst","emzip5","emdoby","emdobm","emdobd","emsex","emms","emphon","file_date"]

class DepnpSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyappDepnp
        fields = ["id","dpclnt","dpssn","dpdoby","dpdobm","dpdobd","dpdssn","dpsex","dptype","dpplan","dpclas","file_date","dpname"]