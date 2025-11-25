import os
from pathlib import Path

class FolderLock:
    def __init__(self, locks_dir: Path, lock_name: str):
        self.lock_path = locks_dir / lock_name
        self._locked = False

    def acquire(self) -> bool:
        """
        Attempt to acquire the lock in a non-blocking way.
        Returns True if the lock was acquired, False otherwise.
        """
        try:
            self.lock_path.mkdir(parents=True, exist_ok=False)
            self._locked = True
            return True
        except FileExistsError:
            return False

    def release(self):
        """Release the lock."""
        if self._locked:
            os.rmdir(self.lock_path)
            self._locked = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
