from django.core.cache import cache
from .models import Service, ClassSchedule, GalleryImage, Testimonial, Trainer, MembershipPlan, Blog

def global_context(request):
    # Try to get data from cache
    global_data = cache.get('global_data')
    if global_data is None:
        global_data = {}
        # Cache the data for 15 minutes
        cache.set('global_data', global_data, 15 * 60)

    return global_data