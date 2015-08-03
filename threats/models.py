from django.db import models


class Visitor(models.Model):
    alienvaultid = models.TextField()

    class Meta:
        ordering = ('alienvaultid',)


class Visit(models.Model):
    visitor = models.ForeignKey(Visitor, related_name='visits')
    address = models.TextField()
    timestamp = models.TextField()
    endpoint = models.TextField()
