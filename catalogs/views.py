from django.http import JsonResponse

from .models import Currency


def rate(request, *args, **kwargs) -> JsonResponse:

    charhcode = request.GET.get('charcode')
    date = request.GET.get('date')

    currency = Currency.objects.filter(charcode__iexact=charhcode, date=date).first()
    if currency:
        response = JsonResponse(
            {
                'charcode': currency.charcode,
                'date': currency.date,
                'rate': currency.rate
            },
            safe=False,
            status=200
        )
    else:
        response = JsonResponse(
            {
                'message': 'Currency does not exist.'
            },
            status=200
        )

    return response

