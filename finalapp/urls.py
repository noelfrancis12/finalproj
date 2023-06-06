from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('loginpg',views.loginpg,name='loginpg'),
    path('admpg',views.admpg,name='admpg'),
    path('login1',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),
    path('addc',views.addc,name='addc'),
    path('addcdb',views.addcdb,name='addcdb'),
    path('showc',views.showc,name='showc'),
    path('deletecat/<int:pk>',views.deletecat,name='deletecat'),
    path('addf',views.addf,name='addf'),
    path('addfdb',views.addfdb,name='addfdb'),
    path('showf',views.showf,name='showf'),
    path('deletef/<int:pk>',views.deletef,name='deletef'),
    path('adde',views.adde,name='adde'),
    path('addedb',views.addedb,name='addedb'),
    path('showe',views.showe,name='showe'),
    path('deletee/<int:pk>',views.deletee,name='deletee'),
    path('editf/<int:pk>',views.editf,name='editf'),
    path('editfdb/<int:pk>',views.editfdb,name='editfdb'),
    path('signup',views.signup,name='signup'),
    path('signupdb',views.signupdb,name='signupdb'),
    path('showu',views.showu,name='showu'),
    path('deleteu/<int:pk>',views.deleteu,name='deleteu'),
    path('userpg',views.userpg,name='userpg'),
    path('accountpg',views.accountpg,name='accountpg'),
    path('eventbooking',views.eventbooking,name='eventbooking'),
    path('eventbookingdb',views.eventbookingdb,name='eventbookingdb'),
    path('bookinglist',views.bookinglist,name='bookinglist'),
    path('deleteevent/<int:pk>',views.deleteevent,name='deleteevent'),
    path('foodbooking',views.foodbooking,name='foodbooking'),
    path('foodbookingdb',views.foodbookingdb,name='foodbookingdb'),
    path('eventrequest/',views.eventrequest,name='eventrequest'),
    path('approve/<int:pk>',views.approve,name='approve'),
    path('reject/<int:pk>',views.reject,name='reject'),
    path('approvef/<int:pk>',views.approvef,name='approvef'),
    path('rejectf/<int:pk>',views.rejectf,name='rejectf'),
    path('approvedbookings/',views.approvedbookings,name='approvedbookings'),
     path('editpage',views.editpage,name='editpage'),
    path('editdetails/<int:pk>',views.editdetails,name='editdetails'),
]