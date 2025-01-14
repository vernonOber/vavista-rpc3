import setuptools


setuptools.setup(
    name='vavista_rpc',
    version='0.0.13',
    author='Conor Dowling, Kevin Gill',
    author_email='vo2521@gmail.com',
    description='VAVista RPC interface',
    long_description='''
    This is a simple Pythonic mechanism for invoking VistA RPCs.
    The code was developed by Conor Dowling as part of the FMQL
    project.
    ''',
    url="https://github.com/vernonOber/vavista-rpc3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        ],
    python_requires='>=3.6',
)

