from setuptools import find_packages, setup

with open("hawkbit_mgt_api/python-client-generated/README.md", "r") as f:
    long_description = f.read()

setup(
    name="hawkbit_mgt_api",
    version="0.0.1",
    description="A python client generator for hawkbit ",
    package_dir={"": "hawkbit_mgt_api/python-client-generated"},
    packages=find_packages(where="hawkbit_mgt_api"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gokul1362/hawkbit_mgt_api.git",
    author="gokul1362",
    author_email="gokulks1362@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2","certifi >= 14.05.14", "six >= 1.10","python_dateutil >= 2.5.3","setuptools >= 21.0.0","urllib3 >= 1.15.1"],
    },
    python_requires=">=3.10",
)