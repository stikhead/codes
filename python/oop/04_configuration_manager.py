class Database:
    connection_limit = 10

    def connect(self):
        print(f"Connected. Limit is {self.connection_limit}")


class RedisCache(Database):
    connection_limit = 1000


db = Database()
db.connect()
redis = RedisCache()
redis.connect()