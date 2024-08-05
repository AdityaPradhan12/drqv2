from setuptools import setup, find_packages

setup(
    name='drqv2',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'hydra-core',
        'numpy',
        'torch',
    ],
)
