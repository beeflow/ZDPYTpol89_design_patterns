import logging

from peewee_sql.models.first_name import FirstName
from peewee_sql.models.last_name import LastName
from peewee_sql.models.user import User


def main() -> None:
    logger = logging.getLogger('peewee')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    users = (
        User.select(User, FirstName, LastName)
        .join(FirstName, on=(User.first_name == FirstName.id))
        .join(LastName, on=(User.last_name == LastName.id))
    )

    for user in users:
        print(user)


if __name__ == '__main__':
    main()
