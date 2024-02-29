from setuptools import find_packages, setup

REQUIREMENTS = ["typing_extensions>=4.10,<5"]
REQUIREMENTS_DEV = ["cogapp>=3.3,<4"]

setup(
    name="typed_sql",
    packages=find_packages(include=["typed_sql"]),
    version="0.0.1",
    description="A strong typed SQL query builder",
    author="Yongda Fan",
    install_requires=REQUIREMENTS,
    extras_require={"dev": REQUIREMENTS_DEV},
)
