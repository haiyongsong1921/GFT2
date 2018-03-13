from django.db import models
from target.models import EvaluationTarget


class L1FactorManager(models.Manager):
    def get_queryset(self):
        return super(L1FactorManager, self).get_queryset()


class SharedL1FactorManager(models.Manager):
    def get_queryset(self):
        return super(SharedL1FactorManager, self).get_queryset().filter(factor_type='S')


class PrivateL1FactorManager(models.Manager):
    def get_queryset(self):
        return super(PrivateL1FactorManager, self).get_queryset().filter(factor_type='P')


class L1Factor(models.Model):
    SHARED = 'S'
    PRIVATE = 'P'
    TYPE = [
        (SHARED, 'Shared'),
        (PRIVATE, 'Private')
    ]

    summary = models.CharField(max_length=512)
    description = models.TextField()
    factor_type = models.CharField(max_length=1,
                                   choices=TYPE,
                                   default=SHARED)
    target_type = models.CharField(max_length=1,
                                   choices=EvaluationTarget.TYPE,
                                   default=EvaluationTarget.TEAM)
    owner = models.CharField(max_length=50)

    objects = L1FactorManager()
    shared = SharedL1FactorManager()
    private = PrivateL1FactorManager()


class L2Factor(models.Model):
    l1_factor = models.ForeignKey('L1Factor', on_delete=models.CASCADE)
    summary = models.CharField(max_length=512)
    description = models.TextField()
    novices = models.TextField()
    advanced_beginners = models.TextField()
    competent = models.TextField()
    proficient = models.TextField()
    expert = models.TextField()
