# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag | [bag.html](https://github.com/ssannejohansson/MS4/blob/main/bag/templates/bag/bag.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-poster-vault-89343956ce2e.herokuapp.com%2Fbag%2F | ![screenshot](documentation/validation/html-bag-bag.png) | |
| checkout | [checkout.html](https://github.com/ssannejohansson/MS4/blob/main/checkout/templates/checkout/checkout.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-poster-vault-89343956ce2e.herokuapp.com%2Fcheckout%2F | ![screenshot](documentation/validation/html-checkout-checkout.png) | |
| checkout | [checkout_success.html](https://github.com/ssannejohansson/MS4/blob/main/checkout/templates/checkout/checkout_success.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-poster-vault-89343956ce2e.herokuapp.com%2Fcheckout%2Fcheckout_success%28A229F1F598DA42B2B68CA39F7362D78A%29 | ![screenshot](documentation/validation/html-checkout-checkout_success.png) | |
| contact | [contact.html](https://github.com/ssannejohansson/MS4/blob/main/contact/templates/contact/contact.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-poster-vault-89343956ce2e.herokuapp.com%2Fcontact%2F | ![screenshot](documentation/validation/html-contact-contact.png) |  |
| home | [index.html](https://github.com/ssannejohansson/MS4/blob/main/home/templates/home/index.html) |https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-poster-vault-89343956ce2e.herokuapp.com%2F| ![screenshot](documentation/validation/html-home-index.png) |  |
| products | [add_product.html](https://github.com/ssannejohansson/MS4/blob/main/products/templates/products/add_product.html) | Validated by direct input | ![screenshot](documentation/validation/html-products-add_product.png) | |
| products | [edit_product.html](https://github.com/ssannejohansson/MS4/blob/main/products/templates/products/edit_product.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-poster-vault-89343956ce2e.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fproducts%2Fedit%2F3%2F | ![screenshot](documentation/validation/html-products-edit_product.png) ![screenshot](documentation/validation/html-products-edit_product2.png) | ⚠️ Since this page demands authorization, the validation by direct input showed errors on the jinja syntaxes. Therefore, I validated it both by direct input and URI to cover everything. |
| products | [product_detail.html](https://github.com/ssannejohansson/MS4/blob/main/products/templates/products/product_detail.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-poster-vault-89343956ce2e.herokuapp.com%2Fproducts%2F4%2F | ![screenshot](documentation/validation/html-products-product_detail.png) | |
| products | [products.html](https://github.com/ssannejohansson/MS4/blob/main/products/templates/products/products.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-poster-vault-89343956ce2e.herokuapp.com%2Fproducts%2F | ![screenshot](documentation/validation/html-products-products.png) |  |
| profiles | [profile.html](https://github.com/ssannejohansson/MS4/blob/main/profiles/templates/profiles/profile.html) |  Validated by direct input| ![screenshot](documentation/validation/html-profiles-profile.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [checkout.css](https://github.com/ssannejohansson/MS4/blob/main/checkout/static/checkout/css/checkout.css) | Validated by direct input | ![screenshot](documentation/validation/css-checkout-checkout.png) |  |
| profiles | [profile.css](https://github.com/ssannejohansson/MS4/blob/main/profiles/static/profiles/css/profile.css) | Validated by direct input | ![screenshot](documentation/validation/css-profiles-profile.png) |  |
| static | [base.css](https://github.com/ssannejohansson/MS4/blob/main/static/css/base.css) | https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthe-poster-vault-89343956ce2e.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv| ![screenshot](documentation/validation/css-static-base.png) |  |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag | [update_remove.js](https://github.com/ssannejohansson/MS4/blob/main/bag/static/bag/js/update_remove.js) |  | ![screenshot](documentation/validation/js-bag-update_remove.png) | |
| checkout | [stripe_elements.js](https://github.com/ssannejohansson/MS4/blob/main/checkout/static/checkout/js/stripe_elements.js) |  | ![screenshot](documentation/validation/js-checkout-stripe_elements.png) | |
| products | [sort-selector.js](https://github.com/ssannejohansson/MS4/blob/main/products/static/products/js/sort-selector.js) |  | ![screenshot](documentation/validation/js-products-sort-selector.png) |  |
| profiles | [countryfield.js](https://github.com/ssannejohansson/MS4/blob/main/profiles/static/profiles/js/countryfield.js) |  | ![screenshot](documentation/validation/js-profiles-countryfield.png) |  |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| MS4 | [settings.py](https://github.com/ssannejohansson/MS4/blob/main/MS4/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/MS4/settings.py) | ![screenshot](documentation/validation/py-MS4-settings.png) | |
| MS4 | [urls.py](https://github.com/ssannejohansson/MS4/blob/main/MS4/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/MS4/urls.py) | ![screenshot](documentation/validation/py-MS4-urls.png) |  |
| bag | [admin.py](https://github.com/ssannejohansson/MS4/blob/main/bag/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/bag/admin.py) |  | Empty file |
| bag | [contexts.py](https://github.com/ssannejohansson/MS4/blob/main/bag/contexts.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/bag/contexts.py) | ![screenshot](documentation/validation/py-bag-contexts.png) |  |
| bag | [models.py](https://github.com/ssannejohansson/MS4/blob/main/bag/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/bag/models.py) |  | Empty file |
| bag | [bag_tools.py](https://github.com/ssannejohansson/MS4/blob/main/bag/templatetags/bag_tools.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/validation/py-bag-bag_tools.png) |  |
| bag | [tests.py](https://github.com/ssannejohansson/MS4/blob/main/bag/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/bag/tests.py) | | Empty file |
| bag | [urls.py](https://github.com/ssannejohansson/MS4/blob/main/bag/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/bag/urls.py) | ![screenshot](documentation/validation/py-bag-urls.png) |  |
| bag | [views.py](https://github.com/ssannejohansson/MS4/blob/main/bag/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/bag/views.py) | ![screenshot](documentation/validation/py-bag-views.png) | |
| checkout | [admin.py](https://github.com/ssannejohansson/MS4/blob/main/checkout/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/checkout/admin.py) | ![screenshot](documentation/validation/py-checkout-admin.png) |  |
| checkout | [forms.py](https://github.com/ssannejohansson/MS4/blob/main/checkout/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/checkout/forms.py) | ![screenshot](documentation/validation/py-checkout-forms.png) |  |
| checkout | [models.py](https://github.com/ssannejohansson/MS4/blob/main/checkout/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/checkout/models.py) | ![screenshot](documentation/validation/py-checkout-models.png) |  |
| checkout | [signals.py](https://github.com/ssannejohansson/MS4/blob/main/checkout/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/checkout/signals.py) | ![screenshot](documentation/validation/py-checkout-signals.png) |  |
| checkout | [tests.py](https://github.com/ssannejohansson/MS4/blob/main/checkout/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/checkout/tests.py) |  | Empty file |
| checkout | [urls.py](https://github.com/ssannejohansson/MS4/blob/main/checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/checkout/urls.py) | ![screenshot](documentation/validation/py-checkout-urls.png) | |
| checkout | [views.py](https://github.com/ssannejohansson/MS4/blob/main/checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/checkout/views.py) | ![screenshot](documentation/validation/py-checkout-views.png) |  |
| checkout | [webhook_handler.py](https://github.com/ssannejohansson/MS4/blob/main/checkout/webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/checkout/webhook_handler.py) | ![screenshot](documentation/validation/py-checkout-webhook_handler.png) |  |
| checkout | [webhooks.py](https://github.com/ssannejohansson/MS4/blob/main/checkout/webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/checkout/webhooks.py) | ![screenshot](documentation/validation/py-checkout-webhooks.png) | |
| contact | [admin.py](https://github.com/ssannejohansson/MS4/blob/main/contact/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/contact/admin.py) | ![screenshot](documentation/validation/py-contact-admin.png)  |
| contact | [forms.py](https://github.com/ssannejohansson/MS4/blob/main/contact/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/contact/forms.py) | ![screenshot](documentation/validation/py-contact-forms.png) |  |
| contact | [models.py](https://github.com/ssannejohansson/MS4/blob/main/contact/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/contact/models.py) | ![screenshot](documentation/validation/py-contact-models.png) |  |
| contact | [tests.py](https://github.com/ssannejohansson/MS4/blob/main/contact/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/contact/tests.py) |  | Empty file |
| contact | [urls.py](https://github.com/ssannejohansson/MS4/blob/main/contact/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/contact/urls.py) | ![screenshot](documentation/validation/py-contact-urls.png) |  |
| contact | [views.py](https://github.com/ssannejohansson/MS4/blob/main/contact/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/contact/views.py) | ![screenshot](documentation/validation/py-contact-views.png) |  |
|  | [custom_storages.py](https://github.com/ssannejohansson/MS4/blob/main/custom_storages.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/custom_storages.py) | ![screenshot](documentation/validation/py--custom_storages.png) | |
| home | [admin.py](https://github.com/ssannejohansson/MS4/blob/main/home/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/home/admin.py) | | Empty file |
| home | [models.py](https://github.com/ssannejohansson/MS4/blob/main/home/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/home/models.py) | | Empty file |
| home | [tests.py](https://github.com/ssannejohansson/MS4/blob/main/home/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/home/tests.py) |  | Empty file |
| home | [urls.py](https://github.com/ssannejohansson/MS4/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.png) |  |
| home | [views.py](https://github.com/ssannejohansson/MS4/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.png) |  |
|  | [manage.py](https://github.com/ssannejohansson/MS4/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) | |
| products | [admin.py](https://github.com/ssannejohansson/MS4/blob/main/products/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/products/admin.py) | ![screenshot](documentation/validation/py-products-admin.png) |  |
| products | [forms.py](https://github.com/ssannejohansson/MS4/blob/main/products/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/products/forms.py) | ![screenshot](documentation/validation/py-products-forms.png) | |
| products | [models.py](https://github.com/ssannejohansson/MS4/blob/main/products/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/products/models.py) | ![screenshot](documentation/validation/py-products-models.png) | |
| products | [tests.py](https://github.com/ssannejohansson/MS4/blob/main/products/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/products/tests.py) |  | Empty file |
| products | [urls.py](https://github.com/ssannejohansson/MS4/blob/main/products/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/products/urls.py) | ![screenshot](documentation/validation/py-products-urls.png) | |
| products | [views.py](https://github.com/ssannejohansson/MS4/blob/main/products/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/products/views.py) | ![screenshot](documentation/validation/py-products-views.png) | |
| products | [widgets.py](https://github.com/ssannejohansson/MS4/blob/main/products/widgets.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/products/widgets.py) | ![screenshot](documentation/validation/py-products-widgets.png) | |
| profiles | [admin.py](https://github.com/ssannejohansson/MS4/blob/main/profiles/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/profiles/admin.py) | | Empty file |
| profiles | [forms.py](https://github.com/ssannejohansson/MS4/blob/main/profiles/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/profiles/forms.py) | ![screenshot](documentation/validation/py-profiles-forms.png) |  |
| profiles | [models.py](https://github.com/ssannejohansson/MS4/blob/main/profiles/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/profiles/models.py) | ![screenshot](documentation/validation/py-profiles-models.png) | |
| profiles | [tests.py](https://github.com/ssannejohansson/MS4/blob/main/profiles/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/profiles/tests.py) | | Empty file |
| profiles | [urls.py](https://github.com/ssannejohansson/MS4/blob/main/profiles/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/profiles/urls.py) | ![screenshot](documentation/validation/py-profiles-urls.png) |  |
| profiles | [views.py](https://github.com/ssannejohansson/MS4/blob/main/profiles/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MS4/main/profiles/views.py) | ![screenshot](documentation/validation/py-profiles-views.png) |  |


## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.png) | ![screenshot](documentation/responsiveness/tablet-profile.png) | ![screenshot](documentation/responsiveness/desktop-profile.png) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Products | ![screenshot](documentation/responsiveness/mobile-products.png) | ![screenshot](documentation/responsiveness/tablet-products.png) | ![screenshot](documentation/responsiveness/desktop-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/responsiveness/mobile-product-details.png) | ![screenshot](documentation/responsiveness/tablet-product-details.png) | ![screenshot](documentation/responsiveness/desktop-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/responsiveness/mobile-bag.png) | ![screenshot](documentation/responsiveness/tablet-bag.png) | ![screenshot](documentation/responsiveness/desktop-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.png) | ![screenshot](documentation/responsiveness/tablet-checkout.png) | ![screenshot](documentation/responsiveness/desktop-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | ![screenshot](documentation/responsiveness/tablet-checkout-success.png) | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | Works as expected |
| Add Product | ![screenshot](documentation/responsiveness/mobile-add-product.png) | ![screenshot](documentation/responsiveness/tablet-add-product.png) | ![screenshot](documentation/responsiveness/desktop-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/responsiveness/mobile-edit-product.png) | ![screenshot](documentation/responsiveness/tablet-edit-product.png) | ![screenshot](documentation/responsiveness/desktop-edit-product.png) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.png) | ![screenshot](documentation/responsiveness/tablet-contact.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/safari-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/safari-login.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome-profile.png) | ![screenshot](documentation/browsers/firefox-profile.png) | ![screenshot](documentation/browsers/safari-profile.png) | Works as expected |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/safari-home.png) | Works as expected |
| Products | ![screenshot](documentation/browsers/chrome-products.png) | ![screenshot](documentation/browsers/firefox-products.png) | ![screenshot](documentation/browsers/safari-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/browsers/chrome-product-details.png) | ![screenshot](documentation/browsers/firefox-product-details.png) | ![screenshot](documentation/browsers/safari-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/browsers/chrome-bag.png) | ![screenshot](documentation/browsers/firefox-bag.png) | ![screenshot](documentation/browsers/safari-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/browsers/chrome-checkout.png) | ![screenshot](documentation/browsers/firefox-checkout.png) | ![screenshot](documentation/browsers/safari-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.png) | ![screenshot](documentation/browsers/firefox-checkout-success.png) | ![screenshot](documentation/browsers/safari-checkout-success.png) | Works as expected |
| Add Product | ![screenshot](documentation/browsers/chrome-add-product.png) | ![screenshot](documentation/browsers/firefox-add-product.png) | ![screenshot](documentation/browsers/safari-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/browsers/chrome-edit-product.png) | ![screenshot](documentation/browsers/firefox-edit-product.png) | ![screenshot](documentation/browsers/safari-edit-product.png) | Works as expected |
| Contact | ![screenshot](documentation/browsers/chrome-contact.png) | ![screenshot](documentation/browsers/firefox-contact.png) | ![screenshot](documentation/browsers/safari-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/safari-404.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Profile | ![screenshot](documentation/lighthouse/mobile-profile.png) | ![screenshot](documentation/lighthouse/desktop-profile.png) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Products | ![screenshot](documentation/lighthouse/mobile-products.png) | ![screenshot](documentation/lighthouse/desktop-products.png) |
| Product Details | ![screenshot](documentation/lighthouse/mobile-product-details.png) | ![screenshot](documentation/lighthouse/desktop-product-details.png) |
| Bag | ![screenshot](documentation/lighthouse/mobile-bag.png) | ![screenshot](documentation/lighthouse/desktop-bag.png) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.png) | ![screenshot](documentation/lighthouse/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop-checkout-success.png) |
| Add Product | ![screenshot](documentation/lighthouse/mobile-add-product.png) | ![screenshot](documentation/lighthouse/desktop-add-product.png) |
| Edit Product | ![screenshot](documentation/lighthouse/mobile-edit-product.png) | ![screenshot](documentation/lighthouse/desktop-edit-product.png) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Products | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](documentation/features/products.png) |
| | Feature is expected to sort products by price and name. | Tested sorting options for price (low-to-high/high-to-low) and name (alphabetical). | Sorting worked correctly for all options. | ![screenshot](documentation/features/product-sorting2.png)![screenshot](documentation/features/product-sorting3.png) |
| | Feature is expected to filter products by category. | Applied category filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/features/product-filtering.png) |
| | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](documentation/features/product-details.png) |
| Shopping Cart | Feature is expected to allow customers to add items to the cart with quantity controls. | Added products to the cart and adjusted quantities. | Items were added successfully, and quantities updated as expected. | ![screenshot](documentation/features/quantity2.png) |
| | Feature is expected to allow customers to view and manage their cart. | Opened the cart page and edited cart contents. | Cart contents were displayed, updated, and removed correctly. | ![screenshot](documentation/features/view-bag.png) |
| Checkout | Feature is expected to display cart items, grand total, and input fields for checkout. | Proceeded to checkout with items in the cart. | Checkout page displayed cart items, total, and input fields as expected. | ![screenshot](documentation/features/checkout.png) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/features/order-confirmation.png)![screenshot](documentation/features/stripe-successful-order.png) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/features/order-confirmation2.png) |
| | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/features/order-confirmation.png) |
| Contact | Feature is expected to allow customers to contact store owners through a contact form | Filled out the form and clicked send | Email confirmation was sent to the customers email. Message was sent to both store owners email and to admin | ![screenshot](documentation/features/contact.png) ![screenshot](documentation/features/contact2.png) ![screenshot](documentation/features/contact3.png) ![screenshot](documentation/features/contact4.png) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/features/profile-management.png) |
| | Feature is expected to remember the shipping address for returning customers. | Completed multiple checkouts as a returning customer. | Shipping address was pre-filled on subsequent purchases. | ![screenshot](documentation/features/remember-credentials.png) |
| Admin Features | Feature is expected to allow the site owner to create new products. | Created new products with valid data (name, price, description, image, category). | Products were added successfully and displayed on the site. | ![screenshot](documentation/features/add-new-product.png) ![screenshot](documentation/features/add-new-product2.png)|
| | Feature is expected to allow the site owner to update product details. | Edited product details as an admin user. | Product updates were saved and displayed correctly. |![screenshot](documentation/features/edit-new-product.png) ![screenshot](documentation/features/edit-new-product2.png) |
| | Feature is expected to allow the site owner to delete products. | Deleted a product from the inventory. | Product was removed successfully from the site. | ![screenshot](documentation/features/delete-new-product.png) ![screenshot](documentation/features/delete-new-product2.png) ![screenshot](documentation/features/delete-new-product3.png)|
| Orders | Feature is expected to allow the site owner to view all orders placed. | Accessed the orders dashboard as an admin user. | All orders were displayed correctly. | ![screenshot](documentation/features/admin-orders.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL  | A custom 404 error page was displayed as expected. | ![screenshot](documentation/responsiveness/desktop-404.png) |
| Security| Non authorized users should not be able to access add/edit product by using the URL for restricted pages | A restricted page URL was entered by both a anonymous user and a logged in non-superuser | Anonymous users was sent to login and non-superusers got an error message. | ![screenshot](documentation/features/url-testing.png)![screenshot](documentation/features/url-testing2.png)  |
| | Users should not be able to brute-force checkout-success.html when they know the order number. | Entered a checkout-success url with a valid order number with a anonymous user. | An error messages was displayed correctly. | ![screenshot](documentation/features/order-success-security.png) |
| | Checkout should not be processed when entering the wrong card number. | Entered a invalid card | An error messages was displayed correctly. | ![screenshot](documentation/features/stripe-declined.png) |



## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. | ![screenshot](documentation/features/product-list.png) |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. | ![screenshot](documentation/features/save-info.png) |
| As a customer | I would like to browse various product categories | so that I can easily find what I'm looking for. | ![screenshot](documentation/features/categories.png) |
| As a customer | I would like to sort products by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. | ![screenshot](documentation/features/product-sorting.png) ![screenshot](documentation/features/product-sorting2.png) |
| As a customer | I would like to filter products by category | so that I can narrow down the products to the types I am most interested in. | ![screenshot](documentation/features/product-filtering.png) |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](documentation/features/product-details.png) |
| As a customer | I would like to add items to my shopping cart using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. | ![screenshot](documentation/features/quantity.png) |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. | ![screenshot](documentation/features/view-bag.png) |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. | ![screenshot](documentation/features/quantity2.png) |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. | ![screenshot](documentation/features/remove-item.png)![screenshot](documentation/features/remove-item2.png)  |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. | ![screenshot](documentation/features/checkout.png) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](documentation/features/order-confirmation2.png) |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](documentation/features/order-confirmation.png) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](documentation/features/stripe.png) |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. | ![screenshot](documentation/features/profile-management.png) |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. | ![screenshot](documentation/features/remember-credentials.png) |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. | ![screenshot](documentation/features/product-management.png)![screenshot](documentation/features/admin-add.png) |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. | ![screenshot](documentation/features/product-management2.png)![screenshot](documentation/features/admin-edit.png) |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](documentation/features/product-management3.png)![screenshot](documentation/features/admin-delete.png) |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. | ![screenshot](documentation/features/admin-orders.png) |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. | ![screenshot](documentation/features/admin-categories.png)![screenshot](documentation/features/admin-categories2.png)![screenshot](documentation/features/admin-categories3.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/browsers/chrome-404.png) |

## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/ssannejohansson/MS4?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/ssannejohansson/MS4/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/ssannejohansson/MS4/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/ssannejohansson/MS4/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/gh-issues-bug.png)

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/ssannejohansson/MS4?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/ssannejohansson/MS4/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

![screenshot](documentation/gh-issues.png)

### Known Issues

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

