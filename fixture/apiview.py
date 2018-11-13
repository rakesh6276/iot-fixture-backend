from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
import json
from .models import Machine,Component,Operation,Stats
from rest_framework.views import APIView
from rest_framework.response import Response
from fixture.serializers import MachineSerializer, OperationSerializer, ComponentSerializer, StatSerializer, StatUpdateSerializer, ComponentSerializer1
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import UpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view




# class StatList(APIView):
#     def get(self, request):
#         stats = Stats.objects.all()
#         data = StatSerializer(stats, many=True).data
#         return Response(data)


class QuerySet(APIView):
    def get(self, request):
       qs = Stats.objects.filter(value__gte=47)
       # qs = Stats.objects.filter(Q(temprature__lte=40 ) | Q(pressure__lte=40))
       #  qs = Stats.objects.filter(temprature = "temprature", temprature__range = (30,70))
       data = StatSerializer(qs, many=True).data
       return Response(data)


class GetMachine(ListAPIView):
    queryset = Machine.objects.all()
    serializer_class= MachineSerializer


class GetOperation(ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

class GetComponent(ListAPIView):
    queryset = Component.objects.all()
    serializer_class= ComponentSerializer


class GetStats(ListAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatSerializer


@api_view(['PUT'])
def editStats(request, pk):
    print (request.data)
    front_id = request.data
    # stat = Stats.objects.all()
    stat = Stats.objects.get(id = front_id['id'])
    serializer = StatUpdateSerializer(stat, request.data)
    if serializer.is_valid():
        print ('VALID SERIALIZER')
        serializer.save()
        return Response("successfully updated", status=status.HTTP_200_OK)
    else:
        return Response("failed to update", status=status.HTTP_200_OK)


@api_view(['GET'])
def Getlist(self):
    queryset = Stats.objects.raw("SELECT id, machine_id, component_id, operation_id, min(created_date) startTime, max(created_date) endTime from fixture_stats group by machine_id, component_id, operation_id")
    # print(queryset)
    serializer = StatSerializer(queryset, many=True)
    return Response(serializer.data)


class putComponents(APIView):

    def get_object(self, pk):
        try:
            return Component.objects.get(pk=pk)
        except Component.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ComponentSerializer1(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ComponentSerializer1(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getComponents(ListAPIView):
    queryset = Component.objects.all()
    serializer_class= ComponentSerializer1

#
# @api_view(['GET'])
# def Getoperation(self):
#     queryset = Machine.objects.all()
#     # print(queryset)
#     serializer= OperationSerializer1(queryset, many=True)
#     return Response(serializer.data)
#     # print(queryset.query)


