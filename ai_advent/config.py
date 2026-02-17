from pathlib import Path

from pydantic import BaseModel, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class DeepSeekConfig(BaseModel):
    """DeepSeek configuration."""

    api_key: str = ""
    base_url: HttpUrl = HttpUrl(url="https://api.deepseek.com")


class Settings(BaseSettings):
    """All app settings."""

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=False,
        env_nested_delimiter="__",
    )
    deepseek: DeepSeekConfig = DeepSeekConfig()


settings = Settings()  # type: ignore[call-arg]
