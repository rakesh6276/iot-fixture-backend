from rest_framework import serializers

from .models import Machine,Operation,Component,Stats

class MachineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Machine
        fields = '__all__'


class OperationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operation
        fields = '__all__'
#
class ComponentSerializer(serializers.ModelSerializer):
    machine = MachineSerializer()

    class Meta:
        model = Component
        fields = (
            'id',
            'name',
            'machine'
    )

class StatSerializer(serializers.ModelSerializer):
    subquery = MachineSerializer(read_only=True, many=True)

    class Meta:
        model = Stats
        # fields = ('id',
        #           'type',
        #           'value',
        #           'subquery',
        #
        #     )
        # depth = 1
        fields = '__all__'


class StatUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ( 'id',
                   'created_date',
                   'type',
                   'value',
                   "machine",
                   "component",
                   "operation"
                   )

class ComponentSerializer1(serializers.ModelSerializer):
    # current_operation = models.CharField(max_length=100)
    machine = MachineSerializer()
    operation = OperationSerializer()

    class Meta:
        model = Component
        fields = (
            'id',
            # 'name',
            'machine',
            # 'current_operation',
            # 'start_time',
            # 'end_time',
            'operation'
        )


# class ComponentSerializer2(serializers.ModelSerializer):
#     machine = MachineSerializer()
#     # component = ComponentSerializer1()
#
#     class Meta:
#         model = Component
#         fields = (
#             'id',
#             # 'name',
#             'machine'
#             # 'Machine_current_operation',
#             # 'machine__created_date',
#             # 'machine__modified_date'
#         )




