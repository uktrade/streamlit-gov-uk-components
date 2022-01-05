import setuptools


def long_description():
    with open('README.md', 'r') as file:
        return file.read()


setuptools.setup(
    name='streamlit-gov-uk-components',
    version='0.0.1',
    author='Department for International Trade',
    author_email='sre@digital.trade.gov.uk',
    description='A collection of Streamlit components that use or are inspired by the GOV.UK Design System',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/uktrade/streamlit-gov-uk-components',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Archiving :: Compression',
    ],
    python_requires='>=3.7.4',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit>=1.3.1',
    ],
)
