# Generated by Django 5.1.1 on 2025-05-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_notification_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(choices=[('ri-dumbbell-line', 'Dumbbell'), ('ri-body-scan-line', 'Body Scan'), ('ri-meditation-line', 'Meditation'), ('ri-boxing-line', 'Boxing'), ('ri-heart-pulse-line', 'Cardio'), ('ri-fire-line', 'Fat Burn'), ('ri-timer-line', 'Timer'), ('ri-run-line', 'Running'), ('ri-user-star-line', 'Muscle Building'), ('ri-lightning-line', 'Energy Boost'), ('ri-sparkling-line', 'Yoga Pose'), ('ri-bear-smile-line', 'Strength Smile'), ('ri-user-line', 'Personal Trainer'), ('ri-calendar-line', 'Schedule'), ('ri-water-flash-line', 'Hydration'), ('ri-arrow-left-right-line', 'Stretching'), ('ri-scale-line', 'Weight Control'), ('ri-check-double-line', 'Checklist Routine'), ('ri-hotel-bed-line', 'Recovery & Rest'), ('ri-blaze-line', 'Cardio Machine'), ('ri-group-line', 'Group Training'), ('ri-flag-line', 'Goal Setting'), ('ri-bar-chart-line', 'Progress Tracking'), ('ri-restaurant-line', 'Nutrition Advice'), ('ri-chat-smile-line', 'Coaching Support')], max_length=50),
        ),
    ]
