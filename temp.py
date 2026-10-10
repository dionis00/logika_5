import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "django_project.settings"
)
django.setup()

from tasks.models import User, Task

user = User.objects.create(
    name="Alice",
    email="alice@example.com",
    role="admin"
)

task = Task.objects.create(
    name="Homework",
    description="Finish Django",
    assigned_user=user
)

task.status = "done"
task.save()