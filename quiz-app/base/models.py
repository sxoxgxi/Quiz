from django.db import models
import uuid

# Create your models here.


class BaseModel(models.Model):
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Categories(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Questions(BaseModel):
    category = models.ForeignKey(
        Categories, related_name='cat', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    score = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question

    def get_answer(self):
        return Answers.objects.filter(question = self)


class Answers(BaseModel):
    question = models.ForeignKey(
        Questions, related_name='fish', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer
