from peewee import Model, MySQLDatabase

from peewee_sql.settings import DATABASE_CONFIG

mysql = MySQLDatabase(**DATABASE_CONFIG)


class BaseModel(Model):
    class Meta:
        database = mysql
        legacy_table_names = False
