# importing the router from the rest_framework installed in settings.py
from rest_framework import routers
from .views import PostViewSet , SubViewSet , CustomerReportViewSet , student_api , student_create
from django.urls import path


# invoking the DefaultRouter() which has all the http verb path url
# initiate a router with routers.DefaultRouter()
router = routers.DefaultRouter()
#we register the general path for the each api request i.e for all http verbs request(post,get,delete,update,create)
# and then register the different view sets with it
# the router registration process uses the router.register method that accepts two arguments:
# the first argument indicates the REST url prefix - in this case
# stores- and a second argument to specify the view set
router.register('api/post', PostViewSet, 'post')
router.register('api/sub' , SubViewSet  , 'subviewset')
router.register('api/cus' , CustomerReportViewSet , 'custom')



# we now invoke the urls of the router to generate all the urls for the api request
# urlpatterns = router.urls


urlpatterns = [
     path( 'student_api' , student_api ),
     path( 'create' , student_create ),
     
    ]



# from django.urls import path
# from blog.views import PostListView , PostDetailView , PostFeaturedView , PostCategoryView

# urlpatterns = [
#  path('' ,  PostListView.as_view() ),
#  path('featured' ,  PostFeaturedView.as_view() ),
#  path('create' ,  PostCreateView.as_view() ),
#  path('<slug>' ,  PostDetailView.as_view() ),

# ]