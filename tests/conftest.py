import sys
from pathlib import Path

# Add project root to Python import path so that tests can import files
sys.path.append(str(Path(__file__).resolve().parent.parent))