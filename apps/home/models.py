from django.db import models


class University(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Department(models.Model):
    dep_no = models.IntegerField(unique=True)
    dep_name = models.CharField(max_length=250)
    university = models.ForeignKey(
        'University',
        on_delete=models.CASCADE,
        related_name='university'
    )
    schoolarshipORgovernment = models.CharField(max_length=250)
    pointType = models.CharField(max_length=250)

    def __str__(self):
        return self.dep_name
    #
    # class Meta:
    #     unique_together = (("dep_name", "university", "schoolarshipORgovernment"))


class Year(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.IntegerField()
    dep_cap = models.CharField(max_length=255)
    min_rank = models.IntegerField()
    min_point = models.FloatField()

    class Meta:
        unique_together = ('department', 'year')

    def __str__(self):
        return str(self.department.dep_no)


class DepName(models.Model):

    department_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.department_name)
