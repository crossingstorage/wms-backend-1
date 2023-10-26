from django.urls import path
from . import views

urlpatterns = [
    path("customers/", views.CustomerList.as_view(), name="customer-list"),
    path("customers/<int:pk>/", views.CustomerDetail.as_view(), name="customer-detail"),
    path("consignees/", views.ConsigneeList.as_view(), name="consignee-list"),
    path(
        "consignees/<int:pk>/", views.ConsigneeDetail.as_view(), name="consignee-detail"
    ),
    path("carriers/", views.CarrierList.as_view(), name="carrier-list"),
    path("carriers/<int:pk>/", views.CarrierDetail.as_view(), name="carrier-detail"),
    path(
        "carrier-addresses/",
        views.CarrierAddressList.as_view(),
        name="carrier-address-list",
    ),
    path(
        "carrier-addresses/<int:pk>/",
        views.CarrierAddressDetail.as_view(),
        name="carrier-address-detail",
    ),
    path("banks/", views.BankList.as_view(), name="bank-list"),
    path("banks/<int:pk>/", views.BankDetail.as_view(), name="bank-detail"),
    path("contacts/", views.ContactList.as_view(), name="contact-list"),
    path("contacts/<int:pk>/", views.ContactDetail.as_view(), name="contact-detail"),
]
