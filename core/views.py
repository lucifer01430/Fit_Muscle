from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Appointment, Subscription, Blog, Comment, Service, ClassSchedule, GalleryImage, Testimonial, Trainer, MembershipPlan
from .forms import AppointmentForm, SubscriptionForm, CommentForm

def home(request):
    appointment_form = AppointmentForm(request.POST or None)
    subscription_form = SubscriptionForm(request.POST or None)
    appointment_message = None
    subscription_message = None

    if request.method == 'POST':
        if 'form_start' in request.POST:
            if appointment_form.is_valid():
                data = appointment_form.cleaned_data
                Appointment.objects.create(
                    full_name=data['full_name'],
                    phone_number=data['phone_number'],
                    email=data['email'],
                    message=data['message']
                )
                appointment_message = 'Your appointment request has been submitted successfully!'
                appointment_form = AppointmentForm()
            else:
                messages.error(request, 'Please correct the errors in the appointment form.')

        if 'footer_subscribe_box' in request.POST:
            if subscription_form.is_valid():
                email = subscription_form.cleaned_data['email']
                Subscription.objects.create(email=email)
                subscription_message = 'Thank you for subscribing!'
                subscription_form = SubscriptionForm()
            else:
                messages.error(request, 'Please correct the errors in the subscription form.')

    services = Service.objects.all()
    gallery = GalleryImage.objects.all()
    testimonials = Testimonial.objects.all()
    membership_plans = MembershipPlan.objects.all()
    trainers = Trainer.objects.all()
    schedules = ClassSchedule.objects.select_related('trainer', 'background').order_by('start_time')
    blogs = Blog.objects.all().order_by('-created_at')[:6]

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    schedule_by_day = {day: [] for day in days}
    for schedule in schedules:
        if schedule.day in schedule_by_day:
            schedule_by_day[schedule.day].append(schedule)

    return render(request, 'core/home.html', {
        'appointment_form': appointment_form,
        'subscription_form': subscription_form,
        'appointment_message': appointment_message,
        'subscription_message': subscription_message,
        'services': services,
        'gallery': gallery,
        'testimonials': testimonials,
        'membership_plans': membership_plans,
        'trainers': trainers,
        'schedule_by_day': schedule_by_day,
        'days': days,
        'row_range': range(4),
        'blogs': blogs,
    })

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.views += 1
    blog.save()

    comment_form = CommentForm(request.POST or None)
    if request.method == 'POST' and 'comment_form' in request.POST:
        if comment_form.is_valid():
            Comment.objects.create(
                blog=blog,
                name=comment_form.cleaned_data['name'],
                email=comment_form.cleaned_data['email'],
                website=comment_form.cleaned_data['website'],
                comment=comment_form.cleaned_data['comment']
            )
            messages.success(request, 'Your comment has been submitted successfully!')
            comment_form = CommentForm()

    return render(request, 'core/blog_page.html', {
        'blog': blog,
        'comments': blog.comments.all(),
        'comment_form': comment_form,
    })

def about(request):
    services = Service.objects.all()
    gallery = GalleryImage.objects.all()
    testimonials = Testimonial.objects.all()
    trainers = Trainer.objects.all()
    return render(request, 'core/about.html', {
        'services': services,
        'gallery': gallery,
        'testimonials': testimonials,
        'trainers': trainers,
    })

def services(request):
    services = Service.objects.all()
    return render(request, 'core/services.html', {
        'services': services,
    })

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', {
        'images': images,
    })

def schedule(request):
    schedules = ClassSchedule.objects.select_related('trainer', 'background').order_by('start_time')
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    schedule_by_day = {day: [] for day in days}
    for schedule in schedules:
        if schedule.day in schedule_by_day:
            schedule_by_day[schedule.day].append(schedule)

    return render(request, 'core/schedule.html', {
        'schedule_by_day': schedule_by_day,
        'days': days,
        'row_range': range(4),
    })

def membership(request):
    plans = MembershipPlan.objects.all()
    return render(request, 'core/membership.html', {
        'plans': plans,
    })

def trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'core/trainers.html', {
        'trainers': trainers,
    })

def contact(request):
    return render(request, 'core/contact.html', {})