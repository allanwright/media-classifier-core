import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='mccore',
    version='0.0.8',
    author='Allan Wright',
    description='media-classifier-core package',
    long_description=long_description,
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    install_requires=[
        'numpy',
        'sklearn'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)