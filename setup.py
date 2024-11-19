from setuptools import find_packages, setup

with open("python-client-generated/README.md", "r") as f:
    long_description = f.read()

setup(
    name="idgenerator",
    version="0.0.10",
    description="An id generator that generated various types and lengths ids",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArjanCodes/2023-package",
    author="ArjanCodes",
    author_email="arjan@arjancodes.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10","certifi >= 14.05.14", "six >= 1.10","python_dateutil >= 2.5.3"
                    "setuptools >= 21.0.0","urllib3 >= 1.15.1"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)