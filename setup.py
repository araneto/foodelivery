from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="foodelivery",
    version="0.0.1",  # major, minor, patch
    description="Delivery App",
    packages=find_packages(exclude="../venv"),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)