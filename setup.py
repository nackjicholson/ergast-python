from setuptools import setup, find_packages

setup(
    name='ergast',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'Cerberus==1.1',
        'requests==2.16.5',
        'six',
        'uritemplate==3.0.0'
    ],
    author="Will Vaughn",
    author_email="willieviseoae@gmail.com",
    description="Python HTTP client to the Ergast Motor Racing Data API",
    long_description="See: http://github.com/nackjicholson/ergast-python",
    license="MIT",
    keywords="ergast formula1 racing motorsports http client",
    url="http://github.com/nackjicholson/ergast-python"
)
