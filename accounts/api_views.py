from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

@csrf_exempt
def user_info_api(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'bio': user.bio,
            'location': user.address, 
            'email': user.email,
            'username': user.username,
            'profile_image_url': user.profile_image.url if user.profile_image else '',
        }
        return JsonResponse(data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
