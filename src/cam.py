import datetime
from pathlib import Path
from typing import Literal

import cv2


def save_picture(
    capture: cv2.VideoCapture,
    out_dir: Path,
    filename_format: str = r"%Y-%m-%d_%H-%M-%S",
    file_type: Literal["png", "jpg"] = "png",
    start_time: str = "00:00:00",
    end_time: str = "23:59:59",
    time_format: str = r"%H:%M:%S",
) -> None:
    """
    Save a picture from the camera if the current time is within the specified time range.

    Args:
        capture (cv2.VideoCapture): OpenCV video capture object for the camera device.
        out_dir (Path): Directory to save the captured image.
        filename_format (str): Format string for the output filename, using datetime directives. Defaults to "%Y-%m-%d_%H-%M-%S".
        file_type (str): Image file extension ("png" or "jpg"). Defaults to "png".
        start_time (str): Start time (as string) for allowed capture period. Defaults to "00:00:00".
        end_time (str): End time (as string) for allowed capture period. Defaults to "23:59:59".
        time_format (str): Format string for parsing start_time and end_time. Defaults to "%H:%M:%S".

    Returns:
        None
    """
    now_dt = datetime.datetime.now()
    now_time = now_dt.time()
    start = datetime.datetime.strptime(start_time, time_format).time()
    end = datetime.datetime.strptime(end_time, time_format).time()

    if start <= now_time <= end:
        _, frame = capture.read()
        now_str = now_dt.strftime(filename_format)
        filepath = out_dir / f"{now_str}.{file_type}"
        cv2.imwrite(str(filepath), frame)
