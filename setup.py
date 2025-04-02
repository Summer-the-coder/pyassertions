from setuptools import setup, find_packages
from pathlib import Path

script_dir = Path(__file__).parent

def get_version():
    with (script_dir / "assertions" / "__init__.py").open("r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"')

setup(
    name="assertions",
    version=get_version(),
    packages=find_packages(),
    install_requires=[],
)