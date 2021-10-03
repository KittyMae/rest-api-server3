import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rest-api-server", 
    version="0.0.3",
    author="Bara D.",
    author_email="KittyMae@seznam.cz",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KittyMae/rest-api-server3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
