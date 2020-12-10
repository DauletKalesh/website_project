# coding=utf-8
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers


GENDER_CHOICES = [
    ['male', u"Male"],
    ['female', u"Female"],
]

REL_CHOICES = [
    ['none', u"undefined"],
    ['single', u"Single"],
    ['in_a_rel', u"In relations"],
    ['engaged', u"Engaged"],
    ['married', u"Married"],
    ['in_love', u"Fall in love"],
    ['complicated', u"Complicated"],
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"User")
    avatar = models.FileField(verbose_name=u"Avatar", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"About yourself")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"City")
    birth_date = models.DateField(null=True, blank=True, verbose_name=u"Birthdate")
    gender = models.CharField(max_length=10, verbose_name=u"Gender", choices=GENDER_CHOICES, default="male")
    relationship = models.CharField(max_length=20, verbose_name=u"Relationships", choices=REL_CHOICES, default="none")


class Post(models.Model):
    datetime = models.DateTimeField(verbose_name=u"Date", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Author", related_name="posts")
    text = models.CharField(max_length=1000, verbose_name=u"Text", null=True, blank=True)
    image = models.FileField(verbose_name=u"Image", null=True, blank=True)

    class Meta:
        ordering = ["-datetime"]


class Comment(models.Model):
    datetime = models.DateTimeField(verbose_name=u"Date", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Author", related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=u"Post", related_name="comments")
    text = models.CharField(max_length=1000, verbose_name=u"Text", null=True, blank=True)

    class Meta:
        ordering = ["datetime"]

















