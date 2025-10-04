# ChronoCap

A Python project for periodically saving camera images based on configurable settings.

## Features

- Periodically saves images from a camera device
- Configurable interval, device ID, file type, and filename format
- Only saves images between specified start and end times each day

## Getting Started

### Prerequisites

- Python 3.13 (see `.python-version` if present)
- [uv](https://github.com/astral-sh/uv) for dependency and environment management

### Installation

Clone this repository:

```bash
git clone https://github.com/naoto-kawakami/chronocap.git
cd chronocap
```

Install all dependencies and create the virtual environment (if not already present) with:

```bash
uv sync
```

This will use Python 3.13 if installed, as specified in `.python-version`, and create `.venv` automatically.

## Usage

Run the main script:

```bash
uv run src/main.py
```

You can modify the configuration in `config/core.yaml`.

## Project Structure

```plaintext
chronocap/
├── .python-version
├── chronocap.code-workspace
├── pyproject.toml
├── README.md
├── uv.lock
├── config/
│   ├── core.yaml
├── img/
├── src/
│   ├── cam.py
│   ├── config.py
│   ├── main.py
```

## License

MIT
