
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def profile_view(request):
    user = request.user  # aynan kirgan user

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.profession = request.POST.get('profession')
        user.address = request.POST.get('address')
        user.telegram = request.POST.get('telegram')
        user.linkedin = request.POST.get('linkedin')
        user.github = request.POST.get('github')
        user.website = request.POST.get('website')
        user.bio = request.POST.get('bio')
        user.workplace = request.POST.get('workplace')
        user.phone_number = request.POST.get('phone_number')
        user.gender = request.POST.get('gender')

        if 'profile_image' in request.FILES:
            user.profile_image = request.FILES['profile_image']

        user.save()
        messages.success(request, 'Maʼlumotlar yangilandi.')
        return redirect('accounts:profile')

    return render(request, 'accounts/account_profile.html', {'user': user})
