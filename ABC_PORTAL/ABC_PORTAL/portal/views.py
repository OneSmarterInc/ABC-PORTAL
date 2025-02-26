from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db import transaction
from .models import MyappDepnp,MyappEmpyp,MyappElghp
from rest_framework.decorators import api_view
import json
from io import BytesIO
import pyodbc
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import shutil, os, re
from datetime import datetime
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .serializers import MyappRecentDataSerializer,SignupSerializer,EmployeeSerializer, LoginSerializer,OTPLoginSerializer,CountSerializer,EmpypSerializer,DepnpSerializer
import pandas as pd
import tempfile
from django.core.files.storage import FileSystemStorage
import mimetypes
from django.conf import settings
from django.utils.encoding import smart_str
from django.utils.timezone import timedelta
from django.utils.timezone import now
from .models import MyappEmpyp,MyappDepnp,MyappElghp,MyappMssqlCountModel,MyappRecentData,MyappMemberCount


        

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyappEmpyp
from .serializers import EmployeeSerializer

class Get_Count(APIView):
    def post(self,request):
        data = request.data
        date = data.get('date')
        db_data = MyappMssqlCountModel.objects.get(date=date)
        serializer  = CountSerializer(db_data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response("Data not found")

@api_view(['GET'])
def search_employee(request):
    name = request.GET.get('name')
    ssn = request.GET.get('ssn')
    member_id = request.GET.get('member_id')

    if name:
        employees = MyappEmpyp.objects.filter(emname__icontains=name)
    elif ssn:
        employees = MyappEmpyp.objects.filter(emssn=ssn)
    elif member_id:
        employees = MyappEmpyp.objects.filter(emmem=member_id)
    else:
        return Response({"error": "Provide either name, ssn, or member_id"}, status=400)

    serializer = EmpypSerializer(employees, many=True)

    return Response({"results": serializer.data})

class GetMemberCountView(APIView):
    def get(self, request):
        file_date = request.GET.get("file_date")

        if not file_date:
            return Response({"error": "file_date is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            file_date = datetime.strptime(file_date, "%Y-%m-%d").date()
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

        record = MyappMemberCount.objects.filter(file_date=file_date).first()

        if not record:
            return Response({"message": "No data found for the given date"}, status=status.HTTP_404_NOT_FOUND)

        response_data = {
            "new_members": record.new_members,
            "dropped_members": record.dropped_members,
            "file_date": record.file_date.strftime("%Y-%m-%d")
        }

        return Response(response_data, status=status.HTTP_200_OK)

class GetMemberAndDependentsView(APIView):
    def get(self, request):
        ssn = request.query_params.get("ssn")

        if not ssn:
            return Response({"error": "SSN is required"}, status=status.HTTP_400_BAD_REQUEST)

        member = MyappEmpyp.objects.filter(emssn=ssn).order_by('-file_date').first()

        if not member:
            return Response({"message": "No members found for the given SSN"}, status=status.HTTP_404_NOT_FOUND)

        dependents = MyappDepnp.objects.filter(dpssn=member.emssn, file_date=member.file_date)

        member_data = EmpypSerializer(member).data
        dependent_data = DepnpSerializer(dependents, many=True).data

        return Response(
            {"member": member_data, "dependents": dependent_data},
            status=status.HTTP_200_OK
        )


@api_view(['POST'])
def add_member(request):

    relationship = request.data.get("Relationship")
    if relationship != "Member":
        return Response(
            {"error": "Only members can be added. Invalid relationship type."}, 
            
        )
    # Extract Fields (SSN is mandatory, others are optional)
    EMSSN = request.data.get("ssn")  # Social Security Number (Required)
    if not EMSSN:
        return Response({"error": "SSN (EMSSN) is required."}, status=400)
    
    if MyappEmpyp.objects.filter(EMSSN=EMSSN).exists():
            return Response({"error": "SSN already exists. Duplicate entries are not allowed."}, status=400)


    try:
        # Extracting fields exactly as per database
        first_name = request.data.get("")
        EMNAME = request.data.get("EMNAME")  # Full Name
        EMSSN = request.data.get("EMSSN")  # Social Security Number
        EMSEX = request.data.get("EMSEX")  # Gender
        EMDOB = request.data.get("EMDOB")  # Date of Birth (YYYY-MM-DD)
        EMADR1 = request.data.get("EMADR1")  # Address
        EMCITY = request.data.get("EMCITY")  # City
        EMST = request.data.get("EMST")  # State
        Country = request.data.get("Country")  # Country (To be merged with Address)
        EMMEM = request.data.get("EMMEM")  # Member ID

        ELPLAN = request.data.get("ELPLAN")  # Plan
        ELCLAS = request.data.get("ELCLAS")  # Class

        # Convert date format
        dob_parsed = datetime.strptime(EMDOB, "%Y-%m-%d") if EMDOB else None

        # Merge Country with Address
        full_address = f"{EMADR1}, {EMCITY}, {EMST}, {Country}".strip()

        # Store in MyappEmpyp Table
        MyappEmpyp_obj, created = MyappEmpyp.objects.update_or_create(
            EMSSN=EMSSN,
            defaults={
                "EMNAME": EMNAME,
                "EMSEX": EMSEX,
                "emdoby": dob_parsed.year if dob_parsed else None,
                "EMDOBM": dob_parsed.month if dob_parsed else None,
                "emdobd": dob_parsed.day if dob_parsed else None,
                "EMADR1": full_address,  # Storing Country inside Address
                "EMCITY": EMCITY,
                "EMST": EMST,
                "EMMEM": EMMEM
            }
        )

        MyappElghp_obj, created = MyappElghp.objects.update_or_create(
            ELSSN=EMSSN,  # Mapping correctly
            defaults={
                "ELPLAN": ELPLAN,
                "ELCLAS": ELCLAS
            }
        )

        return Response({"message": "Member added successfully!", "status": "success"})
    
    except Exception as e:
        return Response({"error": str(e)}, status=400)
        
class GetMemberInfo(APIView):
    def get(self, request):
        name = request.GET.get('name')
        relationship = request.GET.get('relationship')
        ssn = request.GET.get('ssn')

        if not name and not relationship and not ssn:
            return Response("All fields are required")
        
        if relationship.lower() == "member":
            member = MyappEmpyp.objects.filter(emssn=ssn).first()
            if not member:
                return Response({'error': 'Member not found'}, status=404)
            
            dob = self.format_dob(member.emdobm, member.emdobd, member.emdoby)
        
            data = {
                "name": member.emname if member.emname else "name is not available",
                "ssn": member.emssn if member.emssn else "SSN is not available",
                "relationship": relationship,
                "member_id": member.emmem if member.emmem else "member ID is not available",
                "dob": dob if dob else "DOB is not available",
                "address": member.emadr1 if member.emadr1 else "address is not available",
                "state": member.emst if member.emst else "state is not available",
                "city": member.emcity if member.emcity else "city is not available",
                "country": "USA"
            } 
        
        else:
            dependent = MyappDepnp.objects.filter(dpdssn=ssn, dpname__icontains=name).first()
            if not dependent:
                return Response({"error": "Dependent not found"}, status=404)

            dob = self.format_dob(dependent.dpdobm, dependent.dpdobd, dependent.dpdoby)

            member = MyappEmpyp.objects.filter(emssn=dependent.dpssn).first()

            data = {
                "name": dependent.dpname if dependent.dpname else "name is not available",
                "ssn": dependent.dpdssn if dependent.dpdssn else "SSN is not available",
                "relationship": dependent.dptype if dependent.dptype else "relationship is not available",
                "member_id": member.emmem if member and member.emmem else "member ID is not available",
                "dob": dob if dob else "DOB is not available",
                "address": member.emadr1 if member and member.emadr1 else "address is not available",
                "state": member.emst if member and member.emst else "state is not available",
                "city": member.emcity if member and member.emcity else "city is not available",
                "country": "USA"
            }

        return Response(data)      
    
    def format_dob(self, month, day, year):
        if not (month and day and year):
            return None
        try:
            dob = datetime(year, month, day)
            return dob.strftime("%B %d, %Y")
        except ValueError:
            return None
        

class UpdateMemberInfo(APIView):
    def post(self, request):
        # Get fields from the POSTed JSON payload
        name = request.data.get('name')
        relationship = request.data.get('relationship')
        ssn = request.data.get('ssn')
        member_id = request.data.get('member_id')
        dob_str = request.data.get('dob')  # Expected format: "April 15, 1986"
        address = request.data.get('address')
        state = request.data.get('state')
        city = request.data.get('city')
        # country is default 'USA', so we do not need to update it

        # Check that all required fields are provided
        if not all([name, relationship, ssn, member_id, dob_str, address, state, city]):
            return Response({"error": "Missing required fields"}, status=400)

        # Parse the formatted date string into year, month, day
        year, month, day = self.parse_dob(dob_str)
        if not all([year, month, day]):
            return Response({"error": "Invalid date format. Expected format like 'April 15, 1986'"}, status=400)

        if relationship.lower() == "member":
            # Find the member record in MyappEmpyp table
            instance = MyappEmpyp.objects.filter(emssn=ssn, emname__icontains=name).first()
            if not instance:
                return Response({"error": "Member record not found"}, status=404)
            # Update the member's fields
            instance.emname = name
            instance.emssn = ssn
            instance.emmem = member_id
            instance.emdoby = year
            instance.emdobm = month
            instance.emdobd = day
            instance.emadr1 = address
            instance.emst = state
            instance.emcity = city
            instance.save()
            return Response({"message": "Member record updated successfully"})

        else:
            # For dependent records in MyappDepnp
            instance = MyappDepnp.objects.filter(dpdssn=ssn, dpname__icontains=name).first()
            if not instance:
                return Response({"error": "Dependent record not found"}, status=404)
            
            print("Before Update:", instance.__dict__)
            # Update dependent's fields
            with transaction.atomic():
                rows_updated = MyappDepnp.objects.filter(id=instance.id).update(
                    dpname=name,
                    dpdssn=ssn,
                    dptype=relationship,
                    dpdoby=year,
                    dpdobm=month,
                    dpdobd=day,
                )

            year, month, day = self.parse_dob(dob_str)
            print("Parsed DOB:", year, month, day)

            if rows_updated == 0:
                return Response({"error": "Update failed!"}, status=500)
            else:
                # Optionally re-fetch instance to verify changes:
                updated_instance = MyappDepnp.objects.get(id=instance.id)
                print("After Update (using update()):", updated_instance.__dict__)
                return Response({"message": "Dependent record updated successfully"})

    def parse_dob(self, dob_str):
        """
        Parse a DOB string formatted as "April 15, 1986" into (year, month, day).
        Returns a tuple of (year, month, day) or (None, None, None) if parsing fails.
        """
        try:
            dt = datetime.strptime(dob_str, "%B %d, %Y")
            return dt.year, dt.month, dt.day
        except Exception:
            return None, None, None


class MostRecentDataView(APIView):
    def get(self, request):
        latest_entry = MyappRecentData.objects.order_by('-file_date').first()
        if latest_entry:
            latest_date = latest_entry.file_date
            latest_entries = MyappRecentData.objects.filter(file_date=latest_date)
            serializer = MyappRecentDataSerializer(latest_entries, many=True)
            return Response(serializer.data)
        return Response({"message": "No data found"}, status=404)