import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cidereval",
    version="0.0.1",
    author="Michele Cafagna",
    author_email = "michele.cafagna@um.edu.mt",
    description="Python3 package of the original Cider implementation from Xinlei Chen, Hao Fang, Tsung-Yi Lin, and Ramakrishna Vedantam. The code is minimally edited",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michelecafagna26/cider",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: license.txt",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "spacy==3.1.4",
        "jupyter==1.0.0",
    ],
    python_requires='>=3.6',
)
