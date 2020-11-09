from django.db import models


class Grade(models.Model):
    """
    Grade model
    """
    nama = models.CharField(max_length=4)
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Teacher(models.Model):
    """
    Teacher Model
    Defines the attributes of a guru
    """
    nip = models.CharField(max_length=255)
    nama = models.CharField(max_length=255)
    gender = models.CharField(max_length=5)
    tempat_lahir = models.CharField(max_length=255)
    tgl_lahir = models.DateField()
    alamat = models.CharField(max_length=255)
    nuptk = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    bergabung =  models.CharField(max_length=255)
    madrasah_id = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    """
    Student Model
    Defines the attributes of a student
    """
    nisn = models.CharField(max_length=255)
    nama = models.CharField(max_length=255)
    rombel = models.CharField(max_length=10)
    tgl_lahir = models.DateField()
    agama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    nama_ayah = models.CharField(max_length=255)
    nama_ibu = models.CharField(max_length=255)
    pekerjaan_ayah = models.CharField(max_length=255)
    pekerjaan_ibu = models.CharField(max_length=255)
    alamat_ortu = models.CharField(max_length=255)
    nama_wali = models.CharField(max_length=255)
    pekerjaan_wali = models.CharField(max_length=255)
    alamat_wali = models.CharField(max_length=255)
    ajaran = models.CharField(max_length=255)
    jenjang = models.CharField(max_length=255)
    bergabung =  models.CharField(max_length=255)
    kelas_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    grade = models.ForeignKey(
        Grade,
        related_name='grade',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'student'
        verbose_name_plural = 'student'
        
    def __repr__(self):
        return self.nama + ' is added.'
    
    def __str__(self):
        return self.nama


