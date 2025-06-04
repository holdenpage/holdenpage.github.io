import os

REQUIRED_DIRS = [
    'admin',
    'pages',
    'posts',
    'assets/uploads'
]

def test_required_directories_exist():
    for directory in REQUIRED_DIRS:
        assert os.path.isdir(directory), f"Missing required directory: {directory}"

