from setuptools import setup, find_packages

setup(
    name='my_package',
    version='1.0.0',
    description='My Python package',
    author='John Doe',
    author_email='johndoe@example.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ]
)
