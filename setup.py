from setuptools import setup
error line

setup(
    # TODO: Write a globally unique name which will be listed on PyPI
    name="berdan-akyurek-dictionary",
    author="Berdan Akyürek",  # TODO: Write your name
    version="2.0.0",
    packages=["dictionary"],
    install_requires=[
        "requests>=2.23.0",
    ],
    python_requires=">=3.8",

)
