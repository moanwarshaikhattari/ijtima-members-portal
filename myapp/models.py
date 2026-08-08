# myapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    department = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Automatic profile creation signal
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Member(models.Model):
    LOCATION_CHOICES = [
        ("Airoli", "Airoli"),
        ("Bamandongari", "Bamandongari"),
        ("Belapur CBD", "Belapur CBD"),
        ("Digha Gaon", "Digha Gaon"),
        ("Dronagiri", "Dronagiri"),
        ("Gavan", "Gavan"),
        ("Ghansoli", "Ghansoli"),
        ("Indra nagar", "Indra nagar"),
        ("Khandeshwar", "Khandeshwar"),
        ("Kharghar", "Kharghar"),
        ("Kharkopar", "Kharkopar"),
        ("Kopar Khairane", "Kopar Khairane"),
        ("Mansarovar", "Mansarovar"),
        ("Nerul", "Nerul"),
        ("Nhava Sheva", "Nhava Sheva"),
        ("Panvel", "Panvel"),
        ("Rabale", "Rabale"),
        ("Reconda", "Reconda"),
        ("Sanpada", "Sanpada"),
        ("Seawoods", "Seawoods"),
        ("Shematikhar", "Shematikhar"),
        ("Shramitnagar", "Shramitnagar"),
        ("Taloja phase 1", "Taloja phase 1"),
        ("Taloja phase 2", "Taloja phase 2"),
        ("Targhar", "Targhar"),
        ("Thane", "Thane"),
        ("Turbhe", "Turbhe"),
        ("Turbhe ICL", "Turbhe ICL"),
        ("Uran", "Uran"),
        ("Ulwe","Ulwe"),
        ("Vashi", "Vashi"),
    ]
    BLOOD_CHOICES=[
        ("YES", "YES"),
        ("NO", "NO"),
    ]
    PROFESSION_CHOICES = [
        ('Student', 'Student'),
        # ('Working (Private)', 'Working (Private)'),
        ('Govt Job', 'Govt Job'),
        ('Business', 'Business'),
        ('Doctor', 'Doctor'),
        ('Engineer', 'Engineer'),
        ('Teacher', 'Teacher'),
        ('Advocate', 'Advocate'),
        ('Freelancer', 'Freelancer'),
        ('Self Employee', 'Self Employee'),
        ('Jobless', 'Jobless'),
        ('Retired', 'Retired'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    blood_donate = models.CharField(max_length=10, choices=BLOOD_CHOICES, null=True, blank=True)
    profession = models.CharField(max_length=30, choices=PROFESSION_CHOICES, null=True, blank=True)
    # Member add karne wale logged-in user ka Full Name automatically save hoga
    zimmedar_name = models.CharField(max_length=100)
    
    # Optional: Logged-in user ki Foreign Key reference (for better record tracking)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    joined_at = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.name
    def __str__(self):
        return f"{self.name} ({self.mobile})"