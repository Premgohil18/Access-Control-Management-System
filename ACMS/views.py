from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import socket
def Homepage(request):
    return render(request,"index.html")

def Loginpage(request):
    return render(request,"Login.HTML")

def ContactUs(request):
    return render(request,"contact.html")

def Help(request):
    return render(request,"help.html")

def Services(request):
    return render(request,"services.html")

def Getdetails(request):
    return render(request,"getdetails.html")

def run_python_code(request):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip_address = s.getsockname()[0]
    print(local_ip_address)
    s.close()
    result = str("local_ip_address")
    return JsonResponse({'result': local_ip_address})


def get_mac_address(request):
    import uuid
    mac_address = uuid.getnode()
    mac_address_str = ':'.join(("%012X" % mac_address)[i:i+2] for i in range(0, 12, 2))
    if __name__ == '__main__':
        mac_address = get_mac_address()
        print(f"MAC Address: {mac_address}")
        mac = str("mac_address")
    return JsonResponse({'mac': mac_address})

def get_uid(request):
    import uuid
    six_digit_number = str(uuid.uuid4().int)[:6]
    print(six_digit_number)
    uid = str("six_digit_number")
    return JsonResponse({'uid':six_digit_number})   