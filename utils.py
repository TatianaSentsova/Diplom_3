from faker import Faker


class FakeData:
    @staticmethod
    def email():
        fake = Faker()
        email = fake.ascii_free_email()
        return email
