from .models import Employee
from faker import Faker

faker = Faker()


def seed_db(n):
    for i in range(0, n):
        Employee.objects.create(
            name=faker.name(),
            category=faker.category(),
            tag=faker.tag(),
            description=faker.description(),
            price=faker.price(),
            created_at=faker.created_at(),
        )
