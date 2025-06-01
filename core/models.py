from django.db import models
from django.utils.text import slugify

# Icon model to store predefined icon pairs
class Icon(models.Model):
    name = models.CharField(max_length=100)
    default_icon = models.FileField(upload_to='icons/', help_text="Dark/default icon (SVG, PNG, JPG)")
    hover_icon = models.FileField(upload_to='icons/', help_text="Hover/light icon (SVG, PNG, JPG)")

    def __str__(self):
        return self.name

# Trainer model
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='trainers/')
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return self.name

# Service model linking to icons and trainer
class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    long_description = models.TextField()
    duration = models.CharField(max_length=100, help_text="e.g. 4 weeks, 30 mins/session")
    image = models.ImageField(upload_to='services/images/', blank=True, null=True)

    def __str__(self):
        return self.title

class ScheduleBackground(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='schedule_backgrounds/')

    def __str__(self):
        return self.name

# Class Schedule
class ClassSchedule(models.Model):
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
    class_name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    background = models.ForeignKey(ScheduleBackground, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.class_name} on {self.day} at {self.start_time}"

# Gallery
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.caption or "Image"

# Testimonials
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    rating = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.name

# Notifications
class Notification(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MembershipPlan(models.Model):
    title = models.CharField(max_length=100, help_text="E.g. STANDARD PLAN")
    price = models.PositiveIntegerField(help_text="Plan price in INR")
    duration_text = models.CharField(max_length=50, help_text="E.g. /Month, /3 Months")
    image = models.ImageField(upload_to='membership/', help_text="Plan image")
    features = models.TextField(help_text="Add one feature per line", blank=True)

    def feature_list(self):
        return [f.strip() for f in self.features.strip().split('\n') if f.strip()]

    def __str__(self):
        return f"{self.title} - ₹{self.price}{self.duration_text}"

# Model for Appointment Form submissions
class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField(blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.submission_date}"

# Model for Subscription Form submissions
class Subscription(models.Model):
    email = models.EmailField(unique=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.submission_date}"

# Model for Blog Posts
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.CharField(max_length=50)
    description = models.TextField()  # Short excerpt for homepage
    content = models.TextField()  # Full blog content for detail page
    image = models.ImageField(upload_to='blogs/')  # Featured image
    author = models.CharField(max_length=100, default='Admin')
    views = models.PositiveIntegerField(default=0)  # View counter
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Model for Blog Comments
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"