import os

# ------------------------------------------------------------------
#                             CONSTANT
# ------------------------------------------------------------------
PROJECT_ROOT_ABS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THIS_DIR_ABS_PATH = os.path.dirname(os.path.abspath(__file__))
THIS_FILE_BASE_NAME = os.path.splitext(os.path.basename(__file__))[0]
# ------------------------------------------------------------------

def greeting(name: str) -> str:
    print(f'{PROJECT_ROOT_ABS_PATH=}')
    print(f'{THIS_DIR_ABS_PATH=}')
    print(f'{THIS_FILE_BASE_NAME=}')
    return f"Hello {name}"
