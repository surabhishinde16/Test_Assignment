from behave import given, when, then
from myfactoryapp.models import Product 
from django.urls import reverse
import requests

BASE_URL = 'http://localhost:8000'  # Replace with your actual base URL for the API

@given('a product with name "{name}" and category "{category}"')
def step_given_product(context, name, category):
    context.product_data = {
        "name": name,
        "category": category
    }
    response = requests.post(f'{BASE_URL}/products/', json=context.product_data)
    context.product_id = response.json()['id']

@when('I request the product by ID')
def step_when_request_product_by_id(context):
    response = requests.get(f'{BASE_URL}/products/{context.product_id}/')
    context.response_data = response.json()

@then('I should receive a product with name "{name}" and category "{category}"')
def step_then_receive_product_with_details(context, name, category):
    assert context.response_data['name'] == name
    assert context.response_data['category'] == category

@when('I update the product with name "{name}" and category "{category}"')
def step_when_update_product(context, name, category):
    updated_data = {
        "name": name,
        "category": category
    }
    response = requests.put(f'{BASE_URL}/products/{context.product_id}/', json=updated_data)
    context.response_data = response.json()

@then('the product name should be "{name}"')
def step_then_product_name_should_be(context, name):
    assert context.response_data['name'] == name

@then('the product category should be "{category}"')
def step_then_product_category_should_be(context, category):
    assert context.response_data['category'] == category

@when('I delete the product')
def step_when_delete_product(context):
    response = requests.delete(f'{BASE_URL}/products/{context.product_id}/')
    context.response_status_code = response.status_code

@then('the product should no longer exist')
def step_then_product_should_no_longer_exist(context):
    response = requests.get(f'{BASE_URL}/products/{context.product_id}/')
    assert response.status_code == 404

@given('there are {count} products with names "{names}"')
def step_given_multiple_products(context, count, names):
    names = names.split(', ')
    for name in names:
        requests.post(f'{BASE_URL}/products/', json={"name": name, "category": "General"})

@when('I request the list of all products')
def step_when_request_list_of_all_products(context):
    response = requests.get(f'{BASE_URL}/products/')
    context.response_data = response.json()

@then('I should receive a list with {count} products')
def step_then_receive_list_with_count(context, count):
    assert len(context.response_data) == int(count)

@when('I search for products with name "{name}"')
def ste
