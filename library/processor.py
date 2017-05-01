from .models import BookNotification

def get_notification(request):
    return {
        'notifications':"PROCESSOR"
    }