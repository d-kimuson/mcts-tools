from pathlib import Path

from .env import MATCH_DATA_PATH, RECORD_PATH

PROJECT_DIR = Path('.')
DIST_DIR = PROJECT_DIR / 'dist'
if MATCH_DATA_PATH is None:
    raise RuntimeError('Setup MATCH_DATA_PATH')
MATCH_DATA_DIR = Path(MATCH_DATA_PATH)
if RECORD_PATH is None:
    raise RuntimeError('Setup RECORD_PATH')
RECORD_DIR = Path(RECORD_PATH)

SHOT_PATTERNS_PATH = DIST_DIR / 'shot_patterns.json'
