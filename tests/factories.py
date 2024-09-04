import factory
from faker import Faker
from myfactoryapp.models import Product  

# Initialize Faker
faker = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = Product  # Specify the model that the factory will create

    # Define fields with fake data
    name = factory.LazyAttribute(lambda _: faker.word())  # Random product name
    description = factory.LazyAttribute(lambda _: faker.text(max_nb_chars=200))  # Random description
    price = factory.LazyAttribute(lambda _: round(faker.random_number(digits=5), 2))  # Random price
    category = factory.LazyAttribute(lambda _: faker.word())  # Random category
    availability = factory.LazyAttribute(lambda _: faker.boolean())  # Random boolean for availability
