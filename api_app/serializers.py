from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, FieldError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from courseapp.models import Profession, AdditionalInfo, Course
from task_app.models import File, Task, Comment
from users_app.models import Person, City


def dict_to_filter_params(d, prefix=''):
    """
    Translate a dictionary of attributes to a nested set of parameters suitable for QuerySet filtering. For example:

        {
            "name": "Foo",
            "rack": {
                "facility_id": "R101"
            }
        }

    Becomes:

        {
            "name": "Foo",
            "rack__facility_id": "R101"
        }

    And can be employed as filter parameters:

        Device.objects.filter(**dict_to_filter(attrs_dict))
    """
    params = {}
    for key, val in d.items():
        k = prefix + key
        if isinstance(val, dict):
            params.update(dict_to_filter_params(val, k + '__'))
        else:
            params[k] = val
    return params


class BaseModelSerializer(serializers.ModelSerializer):
    display = serializers.SerializerMethodField(read_only=True)

    def get_display(self, obj):
        return str(obj)


#
# Nested serializers
#

class WritableNestedSerializer(BaseModelSerializer):
    """
    Returns a nested representation of an object on read, but accepts only a primary key on write.
    """

    def to_internal_value(self, data):

        if data is None:
            return None

        # Dictionary of related object attributes
        if isinstance(data, dict):
            params = dict_to_filter_params(data)
            queryset = self.Meta.model.objects
            try:
                return queryset.get(**params)
            except ObjectDoesNotExist:
                raise ValidationError(
                    "Related object not found using the provided attributes: {}".format(params)
                )
            except MultipleObjectsReturned:
                raise ValidationError(
                    "Multiple objects match the provided attributes: {}".format(params)
                )
            except FieldError as e:
                raise ValidationError(e)

        # Integer PK of related object
        if isinstance(data, int):
            pk = data
        else:
            try:
                # PK might have been mistakenly passed as a string
                pk = int(data)
            except (TypeError, ValueError):
                raise ValidationError(
                    "Related objects must be referenced by numeric ID or by dictionary of attributes. Received an "
                    "unrecognized value: {}".format(data)
                )

        # Look up object by PK
        queryset = self.Meta.model.objects
        try:
            return queryset.get(pk=int(data))
        except ObjectDoesNotExist:
            raise ValidationError(
                "Related object not found using the provided numeric ID: {}".format(pk)
            )


class NestedCitySerializer(WritableNestedSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class NestedPersonSerializer(WritableNestedSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class NestedProfessionSerializer(WritableNestedSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class NestedFileSerializer(WritableNestedSerializer):
    class Meta:
        model = File
        fields = '__all__'


class NestedAdditionalInfoSerializer(WritableNestedSerializer):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'


class NestedTaskSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')
    files = NestedFileSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'url', 'name', 'start_date', 'end_date', 'status', 'is_active', 'files',
                  'update_at', ]


class NestedCommentSerializer(WritableNestedSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='profession-detail')

    class Meta:
        model = Profession
        fields = ['id', 'url', 'name']


class PersonSerializer(serializers.ModelSerializer):
    city = NestedCitySerializer()
    url = serializers.HyperlinkedIdentityField(view_name='person-detail')

    class Meta:
        model = Person
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'city', 'age', 'avatar', 'email']


class CourseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='course-detail')
    tasks = NestedTaskSerializer(many=True)
    profession = NestedProfessionSerializer()
    person = NestedPersonSerializer()
    addinfo = NestedAdditionalInfoSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'url', 'name', 'location', 'target', 'status', 'level', 'rate', 'start_date', 'end_date',
                  'update_at', 'is_active', 'profession', 'person', 'tasks', 'addinfo']


class TaskSerializer(serializers.ModelSerializer):
    files = NestedFileSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')
    course = CourseSerializer()
    comments = NestedCommentSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'url', 'name', 'start_date', 'end_date', 'status', 'is_active', 'comments', 'files', 'course',
                  'update_at', ]
