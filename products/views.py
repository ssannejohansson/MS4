from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Min, Max
from django.db.models.functions import Lower
from django.forms import inlineformset_factory
from .models import Product, ProductVariant, Category
from .forms import ProductForm, ProductVariantFormSet


# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries"""

    # Annotate each product with min and max price from its variants
    products = Product.objects.all().annotate(
        min_price=Min('variants__price'),
        max_price=Max('variants__price')
    )
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search query")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = Product.objects.annotate(
        min_price=Min('variants__price'),
        max_price=Max('variants__price')
    ).get(pk=product_id)

    variants = product.variants.all()

    context = {
        'product': product,
        'variants': variants,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """Add products to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        formset = ProductVariantFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            product = form.save()
            formset.instance = product
            formset.save()
            messages.success(request, 'Product successfully added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error
            (request, 'Failed to upload product. Please check your form.')
    else:
        form = ProductForm()
        formset = ProductVariantFormSet()

    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """Edit a product and its variants from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    ProductVariantFormSet = inlineformset_factory(
        Product,
        ProductVariant,
        fields=('size', 'price'),
        extra=1,
        can_delete=True
    )

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        formset = ProductVariantFormSet(request.POST, instance=product)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success
            (request, f"Successfully updated product '{product.name}'")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error
            (request, "Failed to update product. Please check the form.")
    else:
        form = ProductForm(instance=product)
        formset = ProductVariantFormSet(instance=product)
        messages.info(request, f"You are editing '{product.name}'")

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'formset': formset,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted.')
    return redirect(reverse('products'))
