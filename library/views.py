from django.views import generic

#Library Views

class IndexView(generic.TemplateView):
    template_name='index.html'
