import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='mccore',
    version='1.0.3',
    author='Allan Wright',
    description='media-classifier-core package',
    long_description=long_description,
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    install_requires=[
        'numpy',
        'sklearn',
        'importlib_resources ; python_version<"3.7"',
        'spacy',
        'titlecase'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    include_package_data=True
)