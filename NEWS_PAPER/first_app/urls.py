from django.urls import path

from django.conf.urls.static import static

from .views import  FormPageView ,SignupPageView, LoginPageView,HomePageView,LogoutView,NewspaperUpdateView, NewspaperDeleteView

from .views import NewspaperDetailsView 




urlpatterns = [



    #path('index/', IndexPageView.as_view(), name='index'),
    path('form/', FormPageView.as_view(), name='form'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('home/', HomePageView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('newspaper_list/', NewspaperListView.as_view(), name='newspaperlist'),
    path('<int:pk>/', NewspaperDetailsView.as_view(), name='newspaperdetails'),
    path('<int:pk>/update/', NewspaperUpdateView.as_view(), name='newspaperupdate'),
    path('<int:pk>/delete/', NewspaperDeleteView.as_view(), name='newspaperdelete'),
]

