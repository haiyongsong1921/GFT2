from django.db import models


class IndividualManager(models.Manager):
    def get_queryset(self):
        return super(IndividualManager, self).get_queryset().filter(target_type='I')


class TeamManager(models.Manager):
    def get_queryset(self):
        return super(TeamManager, self).get_queryset().filter(target_type='T')


class TargetManager(models.Manager):
    def get_queryset(self):
        return super(TargetManager, self).get_queryset()


class EvaluationTarget(models.Model):
    INDIVIDUAL = 'I'
    TEAM = 'T'
    TYPE = [(INDIVIDUAL, 'Individual'),
            (TEAM, 'Team')]

    name = models.CharField(max_length=128, unique=True)
    target_type = models.CharField(max_length=1,
                                   choices=TYPE,
                                   default=INDIVIDUAL)

    individuals = IndividualManager()
    teams = TeamManager()
    objects = TargetManager()
