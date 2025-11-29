from setuptools import setup, find_packages

setup(
    name="jupyter-cell-runtime",
    version="0.1.0",
    description="A simple Jupyter/IPython cell execution timer with customizable color and label.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "colorama>=0.4.4"
    ],
    classifiers=[
        "Framework :: Jupyter",
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
)
