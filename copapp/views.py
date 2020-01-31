# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView

from .models import UserInfo, VictimCoordinates, PoliceCoordinates
from .policeLocation.serializer import SerializerPoliceAddress
from .victimLocation.serializer import SerializerVictimAddress
from .userInfo.serializer import SerializerUserInfoAddress

from rest_framework import status
from rest_framework.response import Response

from push_notifications.models import GCMDevice

from django.shortcuts import render


def home(request):
    pass


class VictimLocation(APIView):
    def get(self, request):
        addressData = VictimCoordinates.objects.all()
        serialize = SerializerVictimAddress(addressData, many=True)
        return Response(serialize.data)

    def post(self, request):
        serializer = SerializerVictimAddress(data=request.data)
        print(serializer.is_valid())
        ph = request.data["phone_number"]
        print("**************************")
        print(ph)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def loadHtml(request, phone_number_vict, phone_number_pol):
    php = phone_number_pol
    phv = phone_number_vict

    victData = VictimCoordinates.objects.all()

    victLat = None
    victLon = None

    polLat = None
    polLon = None

    for i in range(len(victData)):
        if victData[(len(victData)-1)-i].phone_number == phv:
            victLat = victData[(len(victData)-1)-i].latitude
            victLon = victData[(len(victData)-1)-i].longitude
    print(victLat)
    print(victLon)

    polData = PoliceCoordinates.objects.all()

    for i in range(len(polData)):
        if polData[(len(polData)-1)-i].phone_number == php:
            polLat = polData[(len(polData)-1)-i].latitude
            polLon = polData[(len(polData)-1)-i].longitude
    print(polLat)
    print(polLon)

    url ="50;URL='http://192.168.42.231:8000/firstshortestroute/%s/%s'"%(phv,php)

    return render(request, 'shoroute.html', {'vlat': victLat, 'vLon': victLon, 'pLat': polLat, 'pLon': polLon,
                                             'onde': [[polLat, polLon]], 'url':url,'n':max(polLat, victLat), 's':min(polLat, victLat),
                                             'e':max(polLon, victLon),'w':min(polLon, victLon)})


def rastaloder(request):
    l1,pointA,pointB,plat,plon=[],None,None,None,None
    a = PoliceCoordinates.objects.all()
    clat = a[len(a) - 1].latitude
    clon = a[len(a) - 1].longitude
    pointA = (clon, clat)
    kj = VictimCoordinates.objects.all()
    if len(kj) is not 0:
        for i in range(len(kj)):
            plat = kj[len(kj) - 1].latitude
            plon = kj[len(kj) - 1].longitude
            pointB = (plon, plat)
    '''c = shorrout.object.all()
    for t in c:
        cat = spliter(t.name)
        jk = 0
        r = 0
        lor = 0
        for ik in range(int(len(cat) / 2)):
            l1.append([cat[jk], cat[jk + 1]])
            jk += 2'''
    dictionary = {'title': 'closest_service', 'pm': plat, 'pn': plon, 'cm': clat, 'cn': clon, 'coord1':[[[26.20840564295, 78.1884268000654], [26.2084537721547, 78.1888237669996], [26.2086029725627, 78.1896016076139]], [[26.20840564295, 78.1884268000654], [26.2081168673041, 78.1884911730817]], [[26.2091277105301, 78.1917015650614], [26.2088630011909, 78.1906447747095]], [[26.2088630011909, 78.1906447747095], [26.208603104163, 78.1895987131937]], [[26.2091277105304, 78.1917015650614], [26.2087715560067, 78.1920878031596]], [[26.2087715560067, 78.1920878031596], [26.2085838525084, 78.1923935749872]], [[26.2088678140939, 78.1927315333231], [26.208814872156, 78.1928012707575]], [[26.208814872156, 78.1928012707575], [26.2086464203751, 78.1929407456263]], [[26.2085838525087, 78.1923935749872], [26.2088678140939, 78.1927368977412]], [[26.2086993623897, 78.1930373051508], [26.2085646008508, 78.1930855849131]], [[26.2085646008508, 78.1930855849131], [26.2078426613786, 78.192887101446]], [[26.2086464203751, 78.1929407456263], [26.2086993623897, 78.1930373051508]], [[26.2078378484338, 78.192887101446], [26.2078956037588, 78.1932787039622]], [[26.2078956037588, 78.1932787039622], [26.2078907908161, 78.1933484413966]], [[26.2078907908161, 78.1933484413966], [26.2080351790091, 78.1942282059534]], [[26.2080351790091, 78.1942282059534], [26.2080833083669, 78.1945500710352]], [[26.2080833083669, 78.1945500710352], [26.2082806385261, 78.1947378256663]], [[26.2080311756037, 78.1948256492615], [26.2082854514527, 78.1947378256663]], [[26.2081249906821, 78.1888327886927], [26.2081168673041, 78.1884911730817]]]
,
                  'londe': [], 'north': max(plat,clat), 'south': min(plat,clat), 'east': max(plon,clon), 'west': min(plon,clon)}

    return render(request, 'example.html', dictionary)


class PoliceLocation(APIView):
    def get(self, request):
        addressData = PoliceCoordinates.objects.all()
        serialize = SerializerPoliceAddress(addressData, many=True)
        return Response(serialize.data)

    def post(self, request):
        serializer = SerializerPoliceAddress(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfoList(APIView):
    def get(self, request):
        addressData = UserInfo.objects.all()
        serialize = SerializerUserInfoAddress(addressData, many=True)
        return Response(serialize.data)

    def post(self, request):
        serializer = SerializerUserInfoAddress(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
