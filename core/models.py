from django.db import models

# Create your models here.


# моделька воркспейса, в которой находится таск
class Space(models.Model):

    #имя пространства, в котором находится таск
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
#Моделька этапа выполнения (todo/inprogress/done)
class Stage(models.Model):

    #имя этапа
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class Task(models.Model):

    #в ymlке значится как name, но это не name
    title = models.CharField(max_length=255)
    #описание
    description = models.CharField(max_length=255)
    #создано
    # TODO Перенести на структуру пользователя
    creator_id = models.IntegerField()
    #воркспейс
    space_id = models.IntegerField()
    #Стадия
    stage_id = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    assignee_id = models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):

    text = models.CharField(max_length=255)
    #TODO воткнуть модель пользователя
    creator_id = models.IntegerField()
    task_id = models.ManyToManyField(Task)

    def __str__(self):
        return self.text

class Sprint(models.Model):
    name = models.CharField(max_length=255)
    date_begin = models.DateField()
    date_end = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        #возвращаем имя спринта в формате
        return f"{self.name}: {self.dateBegin} - {self.dateEnd}"

