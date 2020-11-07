from django.db.models.signals import post_save
from job.models import Job
from notifications.models import User 
from django.dispatch import receiver
from django.forms.models import model_to_dict

@receiver(post_save, sender=Job)
def notify(sender, instance, created, **kwargs):
    # insert case
    try:
        if created:
            skill_list = instance.skill.split(', ')
            username = set()
            for skill in skill_list:
                user_obj = User.objects.filter(skill__contains=skill)
                for user in user_obj:
                    username.add(user.name)
            for name in username:
                msg = """Hi {}, a job matching your skillset was posted by {} on {} at {} for the role of {}"""\
                    .format(name,instance.company_name,instance.posted_at,instance.location,instance.role)
                print(msg)
                

        # Update case
        # else:                           
           
    except:
        pass