from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework import permissions 
from rest_framework import viewsets , status
# from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView
from .models import Post  , Subscription , CustomerReportRecord , Student
from .serializers import PostSerializer , SubSerializer ,CustomerReportSerializer , StudentSerializer
from rest_framework.parsers import MultiPartParser, FormParser , JSONParser

from django.views.decorators.csrf import csrf_exempt
import io



#Post Viewset
# viewset allows us to perform full CRUD operations api without defining explicit methods for the functionality
#so u dont need to define ur http verbs like 'get', 'post', 'delete','update', 'put'
class PostViewSet(viewsets.ModelViewSet ) :
    
    
    
    #parser classes that will all Files to be parsed and get upload through forms

    queryset = Post.objects.all()
    
    # setting our permissions
    permission_classes = [
        # allow all permissions for now
        permissions.AllowAny        

        # restricted to the users only so in the header there must:
        # header(
        #     'Authourization : Token `The toke value here`'
        # )
        # permissions.IsAuthenticated
    ]

    # we need to define our serializer class up here
    serializer_class = PostSerializer

    # we are overriding the get_queryset() function bcos we want to return the Posts of the only authenticated User/anonymous user (persmission.AllowAny)
    # def get_queryset(self):
        # this will get only the Post of the user
        # return self.request.user.blog_post.all()


    # user here works with Authentication token solely design for the user
    # # it allows us to save the Post owner when we create the Post
    # def perform_create(self  , serializer):
    #    serializer.save(owner = self.request.user)

    # user here works with Authentication token solely design for the user
    # def perform_create(self  , serializer):
    #     print(serializer)
    #     serializer.save(author = self.request.user)

    # overriding the create method of the CreateModelMixin inherited by ModelViewSet
    # def create(self , request , format=None):
              
    #     serializer = PostSerializer(data = request.data)
    #     if serializer.is_valid(): #serializer level validation
    #         # serializer.save(author= self.request.user)
    #         serializer.save()
    #         headers = self.get_success_headers(serializer.data)
    #         print(headers)

            
    #          # to save for a particular owner
    #         #    serializer.save(author = self.request.user)
    #         return Response(serializer.data , status = status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class SubViewSet(viewsets.ModelViewSet):
    # queryset = Subscription.objects.all()
    serializer_class = SubSerializer
    permission_classes = [permissions.AllowAny]
    

    def get_queryset( self ):
        sub_data = Subscription.objects.all()
        print(sub_data)
        return sub_data

    def perform_create(self  , serializer):
        print(serializer)
        print(serializer.is_valid())
        serializer.save()
        





class CustomerReportViewSet(viewsets.ModelViewSet):
    queryset = CustomerReportRecord.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerReportSerializer




# class PostListView(ListAPIView):
#     queryset = Post.objects.order_by('-date_created')
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class PostDetailView(RetrieveAPIView):
#     queryset = Post.objects.order_by('-date_created')
#     serializer_class = PostSerializer
#     permission_classes = [permissions.AllowAny]

# class PostCreateView(APIView):
#     serializer_class = PostSerializer
#     parser_classes = (MultiPartParser , FormParser,)

#     def 

# class PostFeaturedView(ListAPIView):
#     queryset = Post.objects.all().filter(featured = True)
#     serializer_class = PostSerializer
#     permission_classes = [permissions.AllowAny]


 

    

# STUDENT VIEW HERE
  
@csrf_exempt
def student_api(request):
    if ( request.method == "GET" ) :
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content_type="application/json")

    if ( request.method == "POST" ) :
        json_data = request.body
        # print(json_data)
        stream = io.BytesIO(json_data)
        # print(stream)
        python_data = JSONParser().parse(stream)
        # print(python_data)
        serializer = StudentSerializer(data = python_data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created Successfully...'}
            json_data = JSONRenderer().render(res)
            print(json_data)
            return HttpResponse(json_data , content_type="application/json")
    
    if (request.method == "PUT"):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id' , None)
        if id is not None:
            stu =  Student.objects.get(id=id)
            serializer = StudentSerializer(stu , data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {"msg":"data updated successfully"}
                json_data = JSONRenderer().render(res)
                return  HttpResponse(json_data , content_type="application/json")
        res = {'msg':'data not valid'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data  , content_type = "application/json")

    if (request.method == "DELETE" ):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id' , None)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
            except DoesNotExist:
                res =  {"msg":"Student with this id does not exsit"}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data , content_type="application/json")
            stu.delete()
            res = res =  {"msg":"Student has been deleted"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type="application/json")
        res = res =  {"msg":"Please provide some id to delete the student"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data , content_type="application/json")



    return HttpResponse(JSONRenderer().render(serializer.errors) , content_type='application/json' )



    # stu = Student.objects.get(id=1)
    # serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data )


@csrf_exempt
def student_create( request ):
    if request.method == 'POST':
        json_data = request.body
        # print(json_data)
        stream = io.BytesIO(json_data)
        # print(stream)
        python_data = JSONParser().parse(stream)
        # print(python_data)
        serializer = StudentSerializer(data = python_data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created Successfully...'}
            json_data = JSONRenderer().render(res)
            print(json_data)
            return HttpResponse(json_data , content_type="application/json")

    return HttpResponse(JSONRenderer().render(serializer.errors) , content_type='application/json' )



