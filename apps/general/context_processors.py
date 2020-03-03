from apps.products.models import Category


def general_context(request):
    categories = Category.objects.all().order_by('sort')
    return {'categories': categories}