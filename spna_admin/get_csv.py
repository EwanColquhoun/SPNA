import csv

from django.http import HttpResponse


def export_qs_to_csv(model_class = None, qs = None, field_names = None):
    if model_class and not qs:
        qs = model_class.objects.all()
    if qs and not model_class:
        model_class = qs.model

    meta = model_class._meta
    if not field_names:
        field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in qs:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response