import csv
import datetime

from django.http import HttpResponse


def export_qs_to_csv(model_class = None):
    """
    Gets the model and related fields and inputs them into a csv for SPNA admin.
    """
    # Fields at request of client. No payment details allowed.
    fields = [
        'user',
        'user__email',
        'user__first_name',
        'user__last_name',
        'user__date_joined',
        'nursery',
        'fullname',
        'street_address1',
        'town_or_city',
        'postcode',
        'country',
        'phone',
        'subscription',
        'paid_until',
    ]

    # Generate the csv file with datetime
    timestamp = datetime.date.today()

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment; filename=SPNAMembers@{timestamp}.csv"
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(fields)

    # Use the fields to get the data, specifying the model name
    for row in model_class.objects.values(*fields):
        writer.writerow([row[field] for field in fields])
    # return
    return response
