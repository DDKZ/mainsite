from django.contrib.sites.models import Site, RequestSite

def site(request):
    port_string = request.META.get('SERVER_PORT')
    site_info = {
        'protocol': request.is_secure() and 'https' or 'http',
        'port': port_string if port_string != "80" else None
    }
    if Site._meta.installed:
        site_info['domain'] = Site.objects.get_current().domain
    else:
        site_info['domain'] = RequestSite(request).domain
    return site_info

def absolute_uri(request):
    return {'absolute_uri': request.build_absolute_uri(),}