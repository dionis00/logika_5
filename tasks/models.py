from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=[("admin", "Admin"), ("user", "User")], default="user")

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[("in process", "In process"), ("done", "Done"), ("for later", "For later")], default="in process")
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")