from behave import given, when, then
from myfactoryapp.models import Product  
from tests.factories import ProductFactory

@given('a product with name "{name}" and category "{category}"')
def step_given_product(context, name, category):
    context.product = ProductFactory(name=name, category=category)
    context.product.save()

@when('I load the product data')
def step_when_load_product_data(context):
    # This step could involve API calls or other actions to load data
    context.loaded_product = Product.objects.get(id=context.product.id)

@then('the product should have name "{name}" and category "{category}"')
def step_then_verify_product_data(context, name, category):
    assert context.loaded_product.name == name
    assert context.loaded_product.category == category
