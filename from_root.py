import os

def from_root(*paths):
    """Return project root joined with optional sub-paths.

    Placing this file at the repository root makes the project root
    equal to the directory containing this file.
    """
    root = os.path.dirname(os.path.abspath(__file__))
    if paths:
        return os.path.join(root, *paths)
    return root
