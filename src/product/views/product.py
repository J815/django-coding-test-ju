from django.views import generic
from django.core.paginator import Paginator
from product.models import Variant,Product
from product.forms import ProductFilterForm


class CreateProductView(generic.ListView):
    template_name = 'products/create.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10 

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        context['filter_form'] = ProductFilterForm(self.request.GET)
        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        filter_form = ProductFilterForm(self.request.GET)
        
        if filter_form.is_valid():
            title = filter_form.cleaned_data.get('title')
            variant = filter_form.cleaned_data.get('variant')
            price_from = filter_form.cleaned_data.get('price_from')
            price_to = filter_form.cleaned_data.get('price_to')
            date = filter_form.cleaned_data.get('date')

            if title:
                queryset = queryset.filter(title__icontains=title)
            
            if variant:
                queryset = queryset.filter(variants__name__icontains=variant)
            
            if price_from:
                queryset = queryset.filter(variants__price__gte=price_from)
            
            if price_to:
                queryset = queryset.filter(variants__price__lte=price_to)
            
            if date:
                queryset = queryset.filter(created_at__date=date)

        return queryset