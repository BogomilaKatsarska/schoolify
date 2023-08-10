from django.shortcuts import redirect


def redirect_to_index_on_403_middleware(get_response):
    def middleware(*args, **kwargs):
        response = get_response(*args, **kwargs)

        if response.status_code == 403:
            return redirect('index')
        return response

    return middleware
