from neatsprint_lib.settings import ServiceSettings


class Settings(ServiceSettings):
    service_name: str = "chat"
    api_prefix: str = "chat"


settings = Settings()
