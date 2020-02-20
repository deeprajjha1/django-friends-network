from quickstart import models


def orm_bulk_create(n_records):
    instances = [
        models.User.objects.create_user('user' + str(i))
        for i in range(1, n_records)
        ]

    models.User.objects.bulk_create(instances)

orm_bulk_create(1000)
