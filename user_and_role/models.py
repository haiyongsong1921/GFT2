from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class AdminManager(models.Manager):
    def get_queryset(self):
        return super(AdminManager, self).get_queryset().filter(role='A')


class DesignerManager(models.Manager):
    def get_queryset(self):
        return super(DesignerManager, self).get_queryset().filter(role='D')


class OrganizerManager(models.Manager):
    def get_queryset(self):
        return super(OrganizerManager, self).get_queryset().filter(role='O')


class ReviewerManager(models.Manager):
    def get_queryset(self):
        return super(ReviewerManager, self).get_queryset().filter(role='R')


class User(AbstractUser):
    ADMIN = 'A'
    DESIGNER = 'D'
    ORGANIZER = 'O'
    REVIEWER = 'R'
    ROLES = [(ADMIN, 'Admin'),
             (DESIGNER, 'Designer'),
             (ORGANIZER, 'Organizer'),
             (REVIEWER, 'Reviewer')]

    role = models.CharField(max_length=1,
                            choices=ROLES,
                            default=REVIEWER)

    objects = UserManager()
    admins = AdminManager()
    designers = DesignerManager()
    organizers = OrganizerManager()
    reviewers = ReviewerManager()

    def is_admin(self):
        return self.is_superuser or self.role == self.ADMIN

    def is_designer(self):
        return not self.is_superuser and self.role == self.DESIGNER

    def is_organizer(self):
        return not self.is_superuser and self.role == self.ORGANIZER

    def is_reviewer(self):
        return not self.is_superuser and self.role == self.REVIEWER
