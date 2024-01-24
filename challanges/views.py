from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_datas = {
    "january": f"Hai this is Jan and winter.",
    "february": "Hai this is feb and winter.",
    "march": f"Hai this is march and starting summer.",
    "april": "Hai this is april and summer.",
    "may": f"Hai this is may and summer.",
    "june": "Hai this is june and summer.",
    "july": f"Hai this is july and starting rainy.",
    "august": "Hai this is aug and rainy.",
    "september": f"Hai this is set and rainy.",
    "october": "Hai this is oct and spring.",
    "november": f"Hai this is nov and winter.",
    "december": None,
}


def index(request):
    months_data = list(monthly_datas.keys())
    # html_data = ""
    # for month in months_data:
    #     html_data += f"<li><a href={reverse("monthly_challange", args=[month])}>{month}</a></li>"
    # final_html = f"<ul>{html_data}</ul>"
    # return HttpResponse(final_html)
    return render(request, "challanges/index.html", {
         "months": months_data
    })


def monthly_challanges_in_number(request, month):
    months_data = list(monthly_datas.keys())
    if month > 12:
        return HttpResponseNotFound("Invalied month ")
    month_data = months_data[month-1]
    url_path = reverse("monthly_challange", args=[month_data])
    return HttpResponseRedirect(url_path)

def monthly_challange(request, month):
    try:
        challanges_text = monthly_datas[month]
        # response_html_file = render_to_string("challanges/challanges.html")
        # return HttpResponse(response_html_file)
        return render(request, "challanges/challanges.html", {
             "value_text": challanges_text,
             "month_name": month
        })
    except:
        # return HttpResponseNotFound("This month is not there")
        raise Http404("404.html")
    
