# Text Based MMO

A small text-based MMO prototype. This repository currently contains a minimal entrypoint: `main.py`.

## Description

This project is a lightweight, console-based multiplayer-style game prototype focused on text interactions and simple game mechanics. It's suitable as a starting point for expanding into a larger text-driven game.

## Features

- Minimal single-file entrypoint: `main.py`
- Console-based gameplay
- Easy to extend with new commands, game state, and persistence

## Requirements

- Python 3.10+ (recommended)

There is no requirements file provided; install packages as needed when adding dependencies.

## Installation (Windows)

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the environment:

```powershell
venv\Scripts\Activate.ps1
# or (cmd)
venv\Scripts\activate.bat
```

3. If you add dependencies later, install them with:

```bash
pip install -r requirements.txt
```

## Running

From the repository root run:

```bash
python main.py
```

## Development

- Edit `main.py` to add commands, systems, or networking.
- Consider splitting modules into `game/`, `commands/`, and `server/` as features grow.

## Contributing

Contributions are welcome. Open issues or pull requests with small, focused changes:

- New commands or gameplay systems
- Refactors to modularize code
- Tests for game logic


## Contact

For questions or collaboration ideas, open an issue in this repository.
