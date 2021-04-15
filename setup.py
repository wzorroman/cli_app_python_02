from setuptools import setup, find_packages

setup(
        name="contacts",
        py_modules=find_packages(),
        install_requires=[
            "Click",
            "requests",
            ],
        entry_points="""
        [console_scripts]
        contacts=app:cli
        """,
        )