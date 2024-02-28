from setuptools import find_packages, setup

setup(
    name="typed_sql",
    packages=find_packages(include=["typed_sql"]),
    version="0.0.1",
    description="A strong typed SQL query builder",
    author="Yongda Fan",
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    test_suite="test",
)
