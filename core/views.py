from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from .models import (
    Service, ClassSchedule, GalleryImage, Testimonial, Trainer,
    Notification, MembershipPlan, Appointment, Subscription, Blog, Comment
)
from .forms import AppointmentForm, SubscriptionForm, CommentForm

def home(request):
    services = Service.objects.all()
    gallery = GalleryImage.objects.all()
    testimonials = Testimonial.objects.all()
    membership_plans = MembershipPlan.objects.all()
    trainers = Trainer.objects.all()
    blogs = Blog.objects.all().order_by('-created_at')[:6]
    schedules = ClassSchedule.objects.select_related('trainer').order_by('start_time')

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    row_range = range(4)

    schedule_by_day = {day: [] for day in days}
    for schedule in schedules:
        if schedule.day in schedule_by_day:
            schedule_by_day[schedule.day].append(schedule)

    # Forms
    appointment_form = AppointmentForm(request.POST or None)
    success_message = None

    if request.method == 'POST' and appointment_form.is_valid():
        # ✅ Manually save the form data to the Appointment model
        data = appointment_form.cleaned_data
        Appointment.objects.create(
            full_name=data['full_name'],
            phone_number=data['phone_number'],
            email=data['email'],
            message=data['message']
        )
        success_message = "Appointment submitted successfully!"
        appointment_form = AppointmentForm()  # Reset the form

    return render(request, 'core/home.html', {
        'services': services,
        'gallery': gallery,
        'testimonials': testimonials,
        'membership_plans': membership_plans,
        'trainers': trainers,
        'schedule_by_day': schedule_by_day,
        'days': days,
        'row_range': row_range,
        'appointment_form': appointment_form,
        'success_message': success_message,
        'blogs': blogs,
    })


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.views += 1
    blog.save()

    checklist = blog.checklist_list()
    half = len(checklist) // 2
    checklist_left = checklist[:half]
    checklist_right = checklist[half:]

    # Handle comment submission
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to comment.")
            return redirect('login')  # Ensure 'login' URL exists

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.name = request.user.get_full_name() or request.user.username
            comment.email = request.user.email
            comment.save()
            messages.success(request, 'Comment posted successfully!')
            return redirect(request.path)
    else:
        form = CommentForm()

    return render(request, 'core/blog_page.html', {
        'blog': blog,
        'comments': blog.comments.all().order_by('-created_at'),
        'form': form,
        'checklist_left': checklist_left,
        'checklist_right': checklist_right,
        'meta_title': blog.title,
        'meta_image': blog.main_image.url if blog.main_image else None,
    })


def about(request):
    return render(request, 'core/about.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services': services})

def classes(request):
    classes = ClassSchedule.objects.all()
    return render(request, 'core/classes.html', {'classes': classes})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', {'images': images})

def membership(request):
    plans = MembershipPlan.objects.all()
    return render(request, 'core/membership.html', {'plans': plans})

def contact(request):
    return render(request, 'core/contact.html')

def trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'core/trainers.html', {'trainers': trainers})

def notifications(request):
    notes = Notification.objects.order_by('-date')
    return render(request, 'core/notifications.html', {'notifications': notes})
