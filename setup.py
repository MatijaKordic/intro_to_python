from setuptools import find_packages, setup

setup(
    name="intro_to_python",
    version="0.1.0",
    description="A repository for learning Python programming",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MatijaKordic/intro_to_python",
    author="Matija Kordic",
    author_email="matijakordic@rocketmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Education :: Programming :: Beginner",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="python, learning, TDD, exercises, tutorial",  # Optional
)
