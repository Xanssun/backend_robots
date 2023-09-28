from datetime import timedelta, datetime, timezone
import io
from django.shortcuts import render
from django.http import FileResponse
from openpyxl import Workbook
from django.db.models import Count

from robots.models import Robot

def index(request):
    return render(request, 'orders/index.html')

def download(request):
    week_ago = datetime.now(timezone.utc) - timedelta(days=7)
    robots = Robot.objects.filter(created__gte=week_ago)
    report = robots.values('model', 'version').annotate(total=Count("id"))

    workbook = Workbook()

    for model_data in report:
        model = model_data['model']
        version = model_data['version']
        total = model_data['total']

        worksheet = workbook.create_sheet(title=f'{model} {version}')
        worksheet.append(['Model', 'Version', 'Total'])
        worksheet.append([model, version, total])

    default_sheet = workbook.active
    workbook.remove(default_sheet)

    buffer = io.BytesIO()
    workbook.save(buffer)
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='robot_report.xlsx')