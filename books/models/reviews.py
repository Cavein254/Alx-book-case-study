from django.db import models

class Review(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey('books.Customer', on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title} by {self.customer.first_name} {self.customer.last_name} - Rating: {self.rating}"