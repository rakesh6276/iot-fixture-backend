from django.urls import path
from fixture.apiview import QuerySet, GetMachine, GetOperation, GetComponent, GetStats, editStats, Getlist

urlpatterns = [
    path('machine/list/', GetMachine.as_view(), name="machine_list"),
    path('component/list/', GetComponent.as_view(), name="component_list"),
    path('operation/list/', GetOperation.as_view(), name="operation_list"),
    path('stats/list/', GetStats.as_view(), name="stat_list"),
    path('stats/put/<int:pk>/', editStats, name='edit_detail'),
    path('stats/qry/', QuerySet.as_view(), name="query_set"),
    path('stats/list2/', Getlist, name='get_detail')

]