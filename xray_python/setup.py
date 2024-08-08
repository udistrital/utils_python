from setuptools import setup, find_packages

setup(
    name='xray_libreria',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'boto3',
        'aws-xray-sdk',
        'flask'
    ],
    description='Libreria con el sdk y su configuración de xray',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='url del repositorio en github',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)