from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.urls import reverse
# read docs for fields

User = settings.AUTH_USER_MODEL


class Topic(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300, blank=True)
    followers = models.IntegerField(null=True, blank=True, default=0)
    topic_logo = models.FileField()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name + '-' + self.desc

    def get_absolute_url(self):
        return reverse('FeQta:topic_detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name


def slug_pre_save_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_pre_save_receiver, Topic)


class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # what if account is deleted
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.TextField()
    desc = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    follow = models.IntegerField(null=True, blank=True, default=0)
    def get_absolute_url(self):
        return reverse('FeQta:question_detail', kwargs={'slug': self.slug})
    #     return reverse('FeQta:question_detail', kwargs={'slug1':self.topic.slug, 'slug2': self.slug})

    def __str__(self):
        return self.question

    @property
    def title(self):
        return self.pk


pre_save.connect(slug_pre_save_receiver, Question)


class Answer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=20000)
    likes = models.IntegerField(null=True, blank=True, default=0)
    needs_improvement = models.IntegerField(null=True, blank=True, default=0)
    dislikes = models.IntegerField(null=True, blank=True, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated', '-timestamp']

    def get_absolute_url(self):
        return reverse('FeQta:question_detail', kwargs={'slug': self.question.slug})

# contents = models.Textfield(help_text="Seperate by comma")
# def get_contents(self):
#   return self.contents.split(',')

# class Comment(models.Model):
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
#     text = models.CharField(max_length=700)
#     #add reply button
#
#
# class Reply(models.Model):
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     text = models.CharField(max_length=700)
#     #add reply button
#
# class User
