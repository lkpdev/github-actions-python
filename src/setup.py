import setuptools
import os
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lkpdev-github-actions-python", # Replace with your own username
    version= "1.0.0",
    author="Lipika P",
    author_email="lips15sg@gmail.com",
    description="Hellow World Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lkpdev/github-actions-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)