import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="subsurfaceCollabor8", 
    version="0.5",
    author="Subsurface Collabor8 community",
    author_email="ep-domain@norog.no",
    license='Apache License 2.0',
    description="A small example package for working with the Subsurface module of the Collabor8 platform",
    url="https://github.com/digitalcollaboration-collabor8/subsurfaceSampleClient",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas>=1.03',
        'requests>=2.23.0',
        'openpyxl>=3.0.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)