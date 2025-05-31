from django.db import models
import uuid
import random
import string

def generate_plot_id():
    # Generate a random string of 8 characters
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
    # Create plot ID with 'plt' prefix
    plot_id = f"plt{random_str}"
    return plot_id

class Plot(models.Model):
    plot_id = models.CharField(max_length=20, primary_key=True, default=generate_plot_id)
    plot_name = models.CharField(max_length=100)
    plot_location = models.CharField(max_length=255)
    plot_size = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plot_name

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.plot_id:
            # Keep generating until we get a unique plot_id
            while True:
                plot_id = generate_plot_id()
                if not Plot.objects.filter(plot_id=plot_id).exists():
                    self.plot_id = plot_id
                    break
        super().save(*args, **kwargs) 