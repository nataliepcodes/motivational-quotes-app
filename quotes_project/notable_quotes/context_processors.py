# Context_processors is a list of dotted Python paths 
# to callables that are used to populate the context when 
# a template is rendered with a request
# https://docs.djangoproject.com/en/6.0/ref/templates/api/
# Added "notable_quotes.context_processors.categories", in settings.py TEMPLATES "context_processors"


from .models import Category

def categories(request):
    return {
        "categories": Category.objects.all()
    }