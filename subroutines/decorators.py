from django.shortcuts import redirect

def auth_check(view):
    def check(request):
        if request.user.is_authenticated:
            url = str(request.META.get('HTTP_REFERER', 'landing'))
            if 'login' in url: url='landing'
            return redirect(url)
        else: return view(request)
    return check
