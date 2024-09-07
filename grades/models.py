from django.db import models
from django.urls import reverse

# Create your models here.


class StudentRate(models.Model):
    """Model representing a student grade
    at the end of his/her course."""

    student_code = models.CharField(
        max_length=20, help_text="Ingresa el código del estudiante"
    )
    name = models.CharField(
        max_length=200, help_text="Ingresa el nombre del estudiante"
    )
    year = models.IntegerField(null=False)

    period = models.IntegerField(null=False)

    course = models.CharField(max_length=200)

    gender = models.CharField(max_length=20)
    age = models.IntegerField(null=False)
    grade = models.IntegerField(null=False)

    family_size = models.CharField(max_length=200)

    parent_status = models.CharField(max_length=200)
    medu = models.CharField(max_length=200)
    fedu = models.CharField(max_length=200)

    # reason = models.CharField(max_length=200)

    travel_time = models.CharField(max_length=200)
    study_time = models.CharField(max_length=200)

    schoolsup = models.CharField(max_length=200)

    activities = models.CharField(max_length=200)
    higher = models.CharField(max_length=200)

    internet = models.CharField(max_length=200)
    famrel = models.CharField(max_length=200)
    freetime = models.CharField(max_length=200)
    health = models.CharField(max_length=200)
    # absences = models.IntegerField(null=True)
    g1_conduct = models.IntegerField(null=False)
    # r1 = models.IntegerField(null=False)

    gf = models.IntegerField(null=False)

    predicted_evaluation = models.CharField(max_length=100)
    final_evaluation = models.CharField(max_length=100)

    creation_date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse("grades-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return (
            self.student_code
            + " - "
            + self.name
            + " - "
            + self.creation_date.strftime("%Y-%m-%d %H:%M:%S")
        )
