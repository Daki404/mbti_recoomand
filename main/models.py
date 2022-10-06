from django.db import models

class Lectures(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    youtube_link = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'lectures'

class MbtiLecture(models.Model):
    id = models.BigAutoField(primary_key=True)
    lecture_id = models.ForeignKey("Lectures", related_name="lecture", on_delete=models.CASCADE, db_column="lecture_id")
    E_I = models.IntegerField()
    S_N = models.IntegerField()
    T_F = models.IntegerField()
    P_J = models.IntegerField()


