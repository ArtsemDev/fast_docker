from pydantic import BaseSettings, PostgresDsn, RedisDsn, SecretStr, PositiveInt, EmailStr


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    CELERY_BROKER_URL: RedisDsn
    CELERY_RESULT_BACKEND: RedisDsn
    SMTP_PASSWORD: SecretStr
    SMTP_PORT: PositiveInt
    SMTP_HOST: str
    SMTP_USER: EmailStr
