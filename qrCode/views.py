# from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

def qr_scanner_view(request):
    return render(request, 'qr_scanner.html')

@csrf_exempt
def process_qr_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        qr_data = data.get('qr_data', '')

        print(qr_data)

        return render(request, 'qr_scanner.html', {'status': 'success', 'data': qr_data})
    return render(request, 'qr_scanner.html', {'status': 'failed'}, status=400)