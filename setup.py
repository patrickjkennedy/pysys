import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysys",
    version="0.0.1",
    author="Patrick Kennedy",
    author_email="patrickken@gmail.com",
    description="A simple Python package that returns information about the system it is run on.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patrickjkennedy/pysys",
    install_requires=['psutil'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

