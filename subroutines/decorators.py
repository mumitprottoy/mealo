from django.shortcuts import redirect

def auth_check(view):
    def check(request):
        if request.user.is_authenticated:
            return redirect(str(request.META.get('HTTP_REFERER', 'landing')))
        else: return view(request)
    return check