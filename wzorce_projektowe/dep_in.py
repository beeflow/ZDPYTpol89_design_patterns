import json
from abc import ABC, abstractmethod
from uuid import uuid4


class StorageConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query: str) -> None:
        pass

    def get_data(self, obj) -> dict:
        return {name: getattr(obj, name) for name in vars(obj) if not name.startswith("_")}

    @abstractmethod
    def save(self, obj):
        pass


class JsonConnector(StorageConnector):
    def execute(self, query: str) -> None:
        print(query)

    def save(self, obj):
        data = self.get_data(obj)
        data.update({"id": str(uuid4())})
        self.execute(json.dumps(data))

        return data["id"]

    def connect(self):
        print("Json Connector")


class PrintConnector(StorageConnector):

    def connect(self):
        print("Print Connector")

    def execute(self, query: str) -> None:
        pass

    def save(self, obj):
        data = self.get_data(obj)
        data.update({"id": str(uuid4())})

        for key, value in data.items():
            print(f"{key}: {value}")

        return data["id"]


class User:
    __tablename__ = "user"

    def __init__(self, connector: StorageConnector, *args, **kwargs):
        self._connector = connector

        self.id = kwargs.pop("id", None)
        self.username = kwargs.pop("username", None)
        self.email = kwargs.pop("email", None)

    def save(self):
        self._connector.connect()
        self._connector.save(self)


def main() -> None:
    j_connector = JsonConnector()
    p_connector = PrintConnector()

    user = User(p_connector, username="wojtek", email="wojtek@test.com")
    user.save()


if __name__ == '__main__':
    main()
