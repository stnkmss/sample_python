from setuptools import setup, find_packages

setup(
    name="sample",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sample_run = sample.cli:main",
        ],
    }
)
