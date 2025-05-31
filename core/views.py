from django.shortcuts import render
from .models import Service, ClassSchedule, GalleryImage, Testimonial, Trainer, Notification, MembershipPlan

def home(request):
    services = Service.objects.all()
    gallery = GalleryImage.objects.all()
    testimonials = Testimonial.objects.all()
    membership_plans = MembershipPlan.objects.all()  # ✅ Add this line
    schedules = ClassSchedule.objects.select_related('trainer').order_by('start_time')

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    row_range = range(4)

    schedule_by_day = {day: [] for day in days}
    for schedule in schedules:
        if schedule.day in schedule_by_day:
            schedule_by_day[schedule.day].append(schedule)

    return render(request, 'core/home.html', {
        'services': services,
        'gallery': gallery,
        'testimonials': testimonials,
        'schedule_by_day': schedule_by_day,
        'days': days,
        'row_range': row_range,
        'membership_plans': membership_plans  
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
