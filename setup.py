from setuptools import setup, find_packages

setup(
    name="DataUnits",
    version="1.0.0",
    author="Nullocrix",
    author_email="nullocrix@gmail.com",
    description="A Python module for converting binary units and SI to bytes and vice-versa.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nullocrix/DataUnits",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
