from rest_framework import serializers 
from .models import Post  , Subscription , CustomerReportRecord , Student
from django.utils import timezone


class StudentSerializer(serializers.ModelSerializer):
      class Meta:
         model = Student
         fields = "__all__"

      def update(self, instance , validated_data):
         print(instance)
         print(validated_data)
         # instance.id = validated_data('id' , instance.id)
         instance.name = validated_data.get('name' , instance.name)
         instance.roll = validated_data.get('roll' , instance.roll)
         instance.city = validated_data.get('city' , instance.city)
         instance.save()
         return instance
      

      # ANYTIME U CALL serializers.is_valid() it will call the validate_my-field-name-here() method
      # FIELD-LEVEL validation where the field we validating is the roll
      # likewise we can also validate other fields too
      def validate_roll(self , value):
         if ( value < 100):
            raise serializers.ValidationError("Roll number less than 100 are not 100")

         return value


      # ANYTIME U CALL serializers.is_valid() it will call the validate() method
      # OBJECT-LEVEL validation where all form fields data object
      def validate(self , data ):
         if ( data.get('roll') > 200):
            raise serializers.ValidationError("Roll number must not be greater than 200 ")
         if (data.get('name') != 'aiziks'):
            raise serializers.ValidationError("name should be aiziks")
         return data




class PostSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Post
      fields = "__all__"
      lookup_fields = ('slug')



class SubSerializer(serializers.ModelSerializer):

      class Meta:
         model = Subscription
         fields = '__all__'
      


class CustomerReportSerializer(serializers.ModelSerializer):
   #  published = serializers.DateTimeField(required=True)
    
    class Meta:
        model = CustomerReportRecord
        fields = '__all__'
        



class AuthorSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Post
      fields = "__all__"
      

class CategorySerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Post
      fields = "__all__"
      



