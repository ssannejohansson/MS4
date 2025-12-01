from django import forms
from django.forms import inlineformset_factory
from .widgets import CustomClearableFileInput
from .models import Product, ProductVariant, Category


class ProductForm(forms.ModelForm):
    """
    Form to add/edit Products.
    Uses a custom clearable file input for the main product image.
    """

    # Use custom widget for the main product image
    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set categories with friendly names
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        # Add Bootstrap 5 classes to all widgets
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-black rounded-0'


class ProductVariantForm(forms.ModelForm):
    """
    Form for ProductVariant (size + price)
    """

    class Meta:
        model = ProductVariant
        fields = ('size', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap 5 classes to all variant widgets
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-black rounded-0'


# Inline formset to manage multiple variants per product
ProductVariantFormSet = inlineformset_factory(
    Product,
    ProductVariant,
    form=ProductVariantForm,
    extra=1,       # Number of empty variant forms to display
    can_delete=True  # Allow removing variants
)
