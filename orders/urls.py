from django.urls import path

from orders.views import delete_order, AddListView

urlpatterns = [
    path('', AddListView.as_view(), name="list_add_order"),
    path('delete/<int:order_id>/', delete_order, name="delete_order"),
    # path('set-timezone/', set_timezone, name="set_timezone")
]
