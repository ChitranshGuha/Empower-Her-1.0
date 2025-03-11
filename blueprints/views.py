# views.py

from django.shortcuts import render
from .models import User, Housekeeper, HomeCook, Beautician, Caretaker, HostelCook, Laundry, Nanny, PlaySchoolTeacher, ShopAttendant

def available_jobs(request):
    # Get the logged-in user's details
    user = request.user  # Make sure the user is logged in
    skills = [user.skill1, user.skill2, user.skill3]

    jobs = []

    # Check for each skill and fetch jobs from the corresponding table
    for skill in skills:
        if skill:  # Check if skill is not None or empty
            if skill.lower() == 'housekeeper':
                jobs += Housekeeper.objects.all()
            elif skill.lower() == 'homecook':
                jobs += HomeCook.objects.all()
            elif skill.lower() == 'beautician':
                jobs += Beautician.objects.all()
            elif skill.lower() == 'caretaker':
                jobs += Caretaker.objects.all()
            elif skill.lower() == 'hostel cook':
                jobs += HostelCook.objects.all()
            elif skill.lower() == 'laundry':
                jobs += Laundry.objects.all()
            elif skill.lower() == 'nanny':
                jobs += Nanny.objects.all()
            elif skill.lower() == 'play school teacher':
                jobs += PlaySchoolTeacher.objects.all()
            elif skill.lower() == 'shop attendant':
                jobs += ShopAttendant.objects.all()

    # Pass the jobs to the template
    return render(request, 'available_jobs.html', {'jobs': jobs})
