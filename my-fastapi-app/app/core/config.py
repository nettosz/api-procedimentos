from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Api procedimentos departamentais"
    admin_email: str = "noe.gomes@amcel.com.br"
    items_per_page: int = 50

    class Config:
        env_file = ".env"

settings = Settings()