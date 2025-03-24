from setuptools import setup, find_packages

setup(
    name="database_backup_shell",
    version="0.1.0",
    author="Nikita Toropov",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dbbackup = src.shell:main"
        ]
    },
    python_requires=">=3.12"
)