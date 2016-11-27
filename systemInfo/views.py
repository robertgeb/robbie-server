from django.http import HttpResponse

def index(req):
    mem_file = open('/proc/meminfo', 'r')
    return HttpResponse(mem_file.read().replace('\n', '<br>'))
