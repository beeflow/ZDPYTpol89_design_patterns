"""Bardzo brzydki przykład testowania obiektów bazując na QueryManagerStub ;P"""
from ret_car_app.models.base_model import QueryManager
from ret_car_app.models.first_name import FirstName


class QueryManagerStub(QueryManager):
    def __init__(self, model):
        super().__init__(model)

    def get(self, **kwargs):
        return "BLE :P"


def main() -> None:
    FirstName.objects = QueryManagerStub(FirstName)
    print(FirstName.objects.get(name="Rafał"))
    print(FirstName.objects.filter(name="Rafał").first())


if __name__ == '__main__':
    main()
