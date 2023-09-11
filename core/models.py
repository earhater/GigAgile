from django.db import models

# Create your models here.


# моделька воркспейса, в которой находится таск
class Space(models.Model):
    #TODO проверить, что айдишник генерится сам
    id = models.IntegerField(primary_key=True)
    #имя пространства, в котором находится таск
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
#Моделька этапа выполнения (todo/inprogress/done)
class Stage(models.Model):

    id = models.IntegerField(primary_key=True)
    #имя этапа
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name




class Task(models.Model):
    id = models.IntegerField(primary_key=True)
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
        return self.name

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=255)
    #TODO воткнуть модель пользователя
    creator_id = models.IntegerField()
    task_id = models.ManyToManyField(Task)
    def __str__(self):
        return self.text

class Sprint(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    dateBegin = models.DateField()
    dateEnd = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    tasks = models.ManyToManyField(Task)
    def __str__(self):
        #возвращаем имя спринта в формате
        return f"{self.name}: {self.dateBegin} - {self.dateEnd}"

