from setuptools import setup

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="dis5000",
    version="0.0.0",
    license="GPL",
    author="kazukazuprogram",
    packages=["dis5000"],
    package_dir={"dis5000": "src"},
    description="dis5000",
    long_description=long_description,
    install_requires=open("requirements.txt").read().strip().splitlines(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Natural Language :: Japanese",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "dis5000 = dis5000.__main__:main",
        ]
    }
)
