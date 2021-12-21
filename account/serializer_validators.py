
# Field-level validation
# You can specify custom field-level validation by adding .validate_<field_name> methods to your Serializer subclass. These are similar to the .clean_<field_name> methods on Django forms.
# These methods take a single argument, which is the field value that requires validation.
# Your validate_<field_name> methods should return the validated value or raise a serializers.ValidationError
class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value


# Object-level validation
# To do any other validation that requires access to multiple fields, add a method called .validate() to your Serializer subclass. This method takes a single argument, which is a dictionary of field values. It should raise a serializers.ValidationError if necessary, or just return the validated values. For example:
class EventSerializer(serializers.Serializer):
    # expecting this 3 class properties to be passed to the serializer
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data


# Validators
# Individual fields on a serializer can include validators, by declaring them on the field instance, for 
def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

class GameRecord(serializers.Serializer):
    score = serializers.IntegerField(validators=[multiple_of_ten])



# Serializer classes can also include reusable validators that are applied to the complete set of field data. These validators are included by declaring them on an inner Meta class,
class EventSerializer(serializers.Serializer):
    name = serializers.CharField()
    room_number = serializers.IntegerField(choices=[101, 102, 103, 201])
    date = serializers.DateField()

    class Meta:
        # Each room only has one event per day.
        validators = [
            UniqueTogetherValidator(
                queryset=Event.objects.all(),
                fields=['room_number', 'date']
            )
        ]


# Writing .create() methods for nested representations
# If you're supporting writable nested representations you'll need to write .create() or .update() methods that handle saving multiple objects.

# The following example demonstrates how you might handle creating a user with a nested profile object.
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user



# Additional keyword arguments
# There is also a shortcut allowing you to specify arbitrary additional keyword arguments on fields, using the extra_kwargs option. As in the case of read_only_fields, this means you do not need to explicitly declare the field on the serializer.

# This option is a dictionary, mapping field names to a dictionary of keyword argument

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
