from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, FieldError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from SkillDiary import settings
from courseapp.models import Profession, AdditionalInfo, Course
from task_app.models import File, Task, Comment
from users_app.models import Person


class NestedPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'username', 'first_name', 'last_name', 'city', 'age', 'avatar', 'email']


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'description', 'file', 'task', 'additional_info']


class NestedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class NestedAdditionalInfoSerializer(serializers.ModelSerializer):
    files = NestedFileSerializer(many=True)

    class Meta:
        model = AdditionalInfo
        fields = ['id', 'name', 'url', 'note', 'type_info', 'is_active', 'course', 'files']


class AdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = ['id', 'name', 'url', 'note', 'type_info', 'is_active', 'course', 'files']


class AdditionalInfoSerializer(serializers.ModelSerializer):
    files = NestedFileSerializer(many=True)
    class Meta:
        model = AdditionalInfo
        fields = ['id', 'name', 'url', 'note', 'type_info', 'is_active', 'course', 'files']


class NestedTaskSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')
    files = NestedFileSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'url', 'name', 'start_date', 'end_date', 'status', 'is_active', 'files', 'done',
                  'update_at', ]


class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Comment
        fields = ['id', 'url', 'text', 'task', 'is_active']


class NestedCommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ['id', 'url', 'text', 'is_active']


class NestedProfessionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)

    class Meta:
        model = Profession
        fields = ['id', 'name']


class ProfessionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='profession-detail')
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Profession
        fields = ['id', 'url', 'name']


class PersonSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='person-detail')

    class Meta:
        model = Person
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'city', 'age', 'avatar', 'email']


class CourseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='course-detail')
    tasks = NestedTaskSerializer(many=True, read_only=True)
    profession = NestedProfessionSerializer(required=False)
    person = NestedPersonSerializer(read_only=True)
    addinfo = NestedAdditionalInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'url', 'name', 'location', 'target', 'status', 'level', 'rate', 'start_date', 'end_date',
                  'update_at', 'is_active','add_report', 'profession', 'person', 'tasks', 'addinfo']

    def create(self, validated_data):

        profession_id = validated_data['profession']['id']
        validated_data['person'] = self.context['request'].user
        validated_data['profession'] = Profession.objects.get(id=profession_id)
        instance = Course.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        if 'profession' in validated_data:
            profession_data = validated_data.pop('profession')
            validated_data['profession'] = Profession.objects.get(id=profession_data.get('id'))
        validated_data['person'] = Person.objects.get(id=self.context['request'].user.id)
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.target = validated_data.get('target', instance.target)
        instance.status = validated_data.get('status', instance.status)
        instance.level = validated_data.get('level', instance.level)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.profession = validated_data.get('profession', instance.profession)
        instance.person = validated_data.get('person', instance.person)
        instance.add_report = validated_data.get('add_report', instance.add_report)
        instance.save()

        return instance


class CourseWithOutTaskSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='course-detail')
    profession = NestedProfessionSerializer(required=False)
    person = NestedPersonSerializer(read_only=True)
    addinfo = NestedAdditionalInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'url', 'name', 'location', 'target', 'status', 'level', 'rate', 'start_date', 'end_date',
                  'update_at', 'is_active', 'add_report', 'profession', 'person', 'addinfo']

    def create(self, validated_data):
        profession_id = validated_data['profession']['id']
        validated_data['person'] = self.context['request'].user
        validated_data['profession'] = Profession.objects.get(id=profession_id)
        instance = Course.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        if 'profession' in validated_data:
            profession_data = validated_data.pop('profession')
            validated_data['profession'] = Profession.objects.get(id=profession_data.get('id'))

        validated_data['person'] = Person.objects.get(id=self.context['request'].user.id)
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.target = validated_data.get('target', instance.target)
        instance.status = validated_data.get('status', instance.status)
        instance.level = validated_data.get('level', instance.level)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.add_report = validated_data.get('add_report', instance.add_report)
        instance.profession = validated_data.get('profession', instance.profession)
        instance.person = validated_data.get('person', instance.person)
        instance.save()

        return instance


class NestedCourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=False)

    class Meta:
        model = Course
        fields = ['id', 'name', ]


class TaskSerializer(serializers.ModelSerializer):
    files = NestedFileSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')
    course = NestedCourseSerializer(required=False)
    comments = NestedCommentSerializer(many=True, read_only=True)
    user = NestedPersonSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'url', 'name', 'start_date', 'end_date', 'status', 'is_active', 'comments', 'files', 'done',
                  'course', 'user',
                  ]

    def create(self, validated_data):
        course_data = validated_data.pop('course')
        validated_data['user'] = self.context['request'].user
        validated_data['course'] = Course.objects.get(id=course_data.get('id'))
        instance = Task.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        if 'course' in validated_data:
            course_data = validated_data.pop('course')
            validated_data['course'] = Course.objects.get(id=course_data.get('id'))

       # validated_data['user'] = self.context['request'].user
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.done = validated_data.get('done', instance.done)
        instance.course = validated_data.get('course', instance.course)
        #instance.user = validated_data.get('user', instance.user)
        instance.save()

        return instance


class PersonDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['password', 'is_superuser', 'activation_key',
                   'activation_key_expires', 'groups', 'user_permissions']
        model = Person


class ProfessionTaskSerializer(serializers.Serializer):
    profession = serializers.CharField(max_length=200)
    tasks = serializers.ListField(child=serializers.CharField(max_length=200)
                                  )
