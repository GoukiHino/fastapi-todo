class Settings:
    API_PREFIX = "/api/v1"

    # DB_DIALECT = ""
    # DB_USERNAME = ""
    # DB_PASSWORD = ""
    # DB_HOST = ""
    # DB_PORT = ""
    # DATABASE = ""
    # DB_URL = f"{DB_DIALECT}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}"

    DB_URL = "sqlite:///app.db"


settings = Settings()
