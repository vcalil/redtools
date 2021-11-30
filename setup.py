import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redtools",
    version="0.0.1",
    author="vcalil",
    author_email="v.calil@hotmail.com",
    description="It's pip... with git.",
    long_description=long_description,
    url="https://github.com/vcalil/redtools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
