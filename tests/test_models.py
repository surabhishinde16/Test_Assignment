import pytest
from myfactoryapp.models import Product 
from tests.factories import ProductFactory

@pytest.mark.django_db
def test_read_product():
    product = ProductFactory()
    retrieved_product = Product.objects.get(id=product.id)
    assert retrieved_product == product

@pytest.mark.django_db
def test_update_product():
    product = ProductFactory()
    product.name = "Updated Name"
    product.save()
    updated_product = Product.objects.get(id=product.id)
    assert updated_product.name == "Updated Name"

@pytest.mark.django_db
def test_delete_product():
    product = ProductFactory()
    product_id = product.id
    product.delete()
    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(id=product_id)

@pytest.mark.django_db
def test_list_all_products():
    ProductFactory.create_batch(5)
    products = Product.objects.all()
    assert len(products) == 5

@pytest.mark.django_db
def test_find_by_name():
    product = ProductFactory(name="UniqueName")
    found_product = Product.objects.get(name="UniqueName")
    assert found_product == product

@pytest.mark.django_db
def test_find_by_category():
    ProductFactory.create_batch(5, category="Electronics")
    products = Product.objects.filter(category="Electronics")
    assert len(products) == 5

@pytest.mark.django_db
def test_find_by_availability():
    ProductFactory.create_batch(3, availability=True)
    available_products = Product.objects.filter(availability=True)
    assert len(available_products) == 3
