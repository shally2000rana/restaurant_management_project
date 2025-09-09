from django.shortcuts import render

def about(request):
    context={
        "history": "Our restaurant was founded in 1995 with the vision of serving authentic, locally sourced meals.",
        "mission": "To provide our customers with high-quality, freshly prepared food in a welcoming atmosphere.",
        "values":[
            "Fresh & Local Ingredients",
            "Excellence Customer Service",
            "Sustainability & Community Support"
        ]
    }
    return render(request, "about.html", context)

