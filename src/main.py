import time
from pathlib import Path
from typing import Any, Callable

import cv2
import schedule

from cam import save_picture
from config import Config


def job(
    params: dict[str, Any],
) -> Callable[[], None]:
    return lambda: save_picture(**params)


def main() -> None:
    src_dir = Path(__file__).resolve().absolute().parent
    project_dir = src_dir.parent
    config_dir = project_dir / "config"
    config_path = config_dir / "core.yaml"
    encoding = "utf-8"
    config = Config.from_yaml(config_path, encoding=encoding)

    out_dir = project_dir / "img"
    out_dir.mkdir(parents=True, exist_ok=True)

    capture = cv2.VideoCapture(config.device_id)
    params = dict(
        capture=capture,
        out_dir=out_dir,
        filename_format=config.filename_format,
        file_type=config.file_type,
        start_time=config.start_time,
        end_time=config.end_time,
        time_format=config.time_format,
    )

    try:
        print("Starting scheduled job...")
        schedule.every(config.interval_minutes).minutes.do(job(params))
        print("Press Ctrl+C to stop.")

        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        capture.release()

    print("Stopped.")


if __name__ == "__main__":
    main()
