from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student, Teacher, Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade 
        fields = ['id','nama', 'level','created_at','updated_at']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'nama']

class StudentSerializer(serializers.ModelSerializer):
    # grade = GradeSerializer(many=True)
    # grade_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        # fields = "__all__"
        # fields = ['id', 'nisn', 'nama', 'rombel', 'tgl_lahir', 'nama_ibu', 'nama_ayah', 'nama_ayah','nama_ibu', 'alamat','pekerjaan_ayah', 'pekerjaan_ibu','agama', 'alamat_ortu', 'nama_wali','pekerjaan_wali','alamat_wali', 'ajaran', "kelas_id", 'jenjang','bergabung','created_at','updated_at', 'grade_id']
