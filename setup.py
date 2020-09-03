import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="failstodeliver",
    version="0.0.1",
    license='MIT',
    author="Yuvraj Chandra",
    author_email="Singhyuvraj179@gmail.com",
    description="A simple package to download failstodeliver data from SEC EDGAR Databse",
    long_description=long_description,
    url="https://github.com/Yuvrajchandra/failstodeliver",
    keywords = ['EDGAR', 'SEC', 'failstodeliver', 'Database'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[            # I get to this in a second
          'requests',
          'beautifulsoup4',
      ],
    python_requires='>=3.6',
)
