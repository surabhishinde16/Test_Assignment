import pytest
from myfactoryapp.models import Product  
from tests.factories import ProductFactory
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_read_product(api_client):
    product = ProductFactory()
    response = api_client.get(f'/products/{product.id}/')
    assert response.status_code == 200
    assert response.data['id'] == product.id

@pytest.mark.django_db
def test_update_product(api_client):
    product = ProductFactory()
    updated_data = {"name": "Updated Name"}
    response = api_client.put(f'/products/{product.id}/', updated_data)
    assert response.status_code == 200
    assert response.data['name'] == "Updated Name"

@pytest.mark.django_db
def test_delete_product(api_client):
    product = ProductFactory()
    response = api_client.delete(f'/products/{product.id}/')
    assert response.status_code == 204
    assert Product.objects.filter(id=product.id).count() == 0

@pytest.mark.django_db
def test_list_all_products(api_client):
    ProductFactory.create_batch(5)
    response = api_client.get('/products/')
    assert response.status_code == 200
    assert len(response.data) == 5

@pytest.mark.django_db
def test_list_by_name(api_client):
    ProductFactory(name="UniqueName")
    response = api_client.get('/products/', {'name': 'UniqueName'})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == "UniqueName"

@pytest.mark.django_db
def test_list_by_category(api_client):
    ProductFactory.create_batch(5, category="Electronics")
    response = api_client.get('/products/', {'category': 'Electronics'})
    assert response.status_code == 200
    assert len(response.data) == 5

@pytest.mark.django_db
def test_list_by_availability(api_client):
    ProductFactory.create_batch(3, availability=True)
    response = api_client.get('/products/', {'availability': True})
    assert response.status_code == 200
    assert len(response.data) == 3
