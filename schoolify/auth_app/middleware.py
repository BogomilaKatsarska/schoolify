from django.shortcuts import redirect


def redirect_to_500_on_500_middleware(get_response):
    def middleware(*args, **kwargs):
        response = get_response(*args, **kwargs)

        if response.status_code == 500:
            return redirect('500')
        return response

    return middleware
