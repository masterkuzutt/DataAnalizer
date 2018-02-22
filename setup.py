from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#     long_description = f.read()


setup(

    name='danalyzer', # Required 
    version='0.0.1',  # Required
    description='A sample Python project that mainly manage data from excel',  # Required
    # long_description=long_description,  # Optional
    url='https://github.com/masterkuzutt/danalyzer',  # Optional
    author='Takahiro Sakai',  # Optional
    author_email='masterkuzutt+github@gmail.com',  # Optional
    test_suite="tests",
    # classifiers=[  # Optional
    #     'Development Status :: 3 - Alpha',
    #     'Intended Audience :: Developers',
    #     'Topic :: Software Development :: Build Tools',
    #     'License :: OSI Approved :: MIT License',
    #     'Programming Language :: Python :: 3.6',
    # ],
    # keywords='sample setuptools development',  # Optional

    packages=find_packages(exclude=['docs', 'tests']),  # Required

    # use requirements.txt
    # install_requires=['numpy'],  # Optional 

    # extras_require={  # Optional
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # data_files=[('my_data', ['data/data_file'])],  # Optional

    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },

    # project_urls={  # Optional
    #     'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #     'Funding': 'https://donate.pypi.org',
    #     'Say Thanks!': 'http://saythanks.io/to/example',
    #     'Source': 'https://github.com/pypa/sampleproject/',
    # },
)