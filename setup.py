from setuptools import setup, find_packages

setup(
    name='ml_model',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas==2.2.2',
        'scikit-learn==1.4.2',
        'mlflow==2.13.0'
    ],
)
