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
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=20, choices=[
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    background = models.ForeignKey(ScheduleBackground, on_delete=models.SET_NULL, null=True, blank=True)  # ✅ NEW

    def __str__(self):
        return f"{self.name} ({self.day} {self.start_time} - {self.end_time})"




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

class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField(blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.submission_date.strftime('%Y-%m-%d')}"
    

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Blog(models.Model):
    # Basic metadata
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.CharField(max_length=100)

    # Hero banner image (for top section of blog detail page)
    banner_image = models.ImageField(upload_to='blogs/banner/', blank=True, null=True,
                                     help_text="This image appears in the blog hero/banner section")

    # Intro & Main image (content image)
    intro_text = models.TextField(help_text="Short intro paragraph shown in hero section")
    main_image = models.ImageField(upload_to='blogs/', help_text="Main image used within blog content")

    # Main blog body
    content_section = models.TextField(help_text="Main HTML content block (use linebreaks or WYSIWYG)")

    # Highlighted quote section
    quote = models.CharField(max_length=300, blank=True)
    quote_author = models.CharField(max_length=100, blank=True)

    # Checklist area (split into left/right)
    checklist_items = models.TextField(help_text="One checklist item per line", blank=True)

    # Optional gallery images
    gallery_image1 = models.ImageField(upload_to='blogs/gallery/', blank=True, null=True)
    gallery_image2 = models.ImageField(upload_to='blogs/gallery/', blank=True, null=True)
    gallery_image3 = models.ImageField(upload_to='blogs/gallery/', blank=True, null=True)

    # System metadata
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def checklist_list(self):
        """Returns checklist items as a clean list (split by line)."""
        return [i.strip() for i in self.checklist_items.strip().split('\n') if i.strip()]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.blog.title}"
