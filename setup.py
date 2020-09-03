from setuptools import setup, find_packages
# run this module with 'sdist upload -r local'
setup(
    name="pythonfakerextensions",
    version="1.0.0",
    packages=find_packages(),
    author="Home Office",
    url="https://github.com/UKHomeOffice/PythonFakerExtensions",
    description="Extension of Faker project with new providers",
    keywords="faker synthetic mock data",
    python_requires=">=3",
    install_requires=[
        'faker==4.0.2',
        'rstr==2.2.6',
        'py-dateutil==2.2'
    ]
)
