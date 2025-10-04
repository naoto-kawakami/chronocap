from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from yaml import safe_load


class Config(BaseModel):
    interval_minutes: int = Field(
        1, ge=0, description="Interval in minutes, must be >= 0"
    )
    device_id: int = Field(0, ge=0, description="Device ID, must be >= 0")
    filename_format: str = r"%Y-%m-%d_%H-%M-%S"
    file_type: Literal["png", "jpg"] = "png"
    start_time: str
    end_time: str
    time_format: str = r"%H:%M:%S"

    @classmethod
    def from_yaml(
        cls,
        path: str | Path,
        encoding: str = "utf-8",
    ) -> Config:
        with open(path, mode="r", encoding=encoding) as f:
            data = safe_load(f)
        return cls(**data)
