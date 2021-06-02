from django.db import models


class Ticket(models.Model):
    subject = models.CharField(max_length=256)
    text = models.TextField()
    status = models.CharField(max_length=16)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket {self.subject} with status {self.status}"


class Comment(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment if Ticket(id={self.ticket_id}): {self.text}"