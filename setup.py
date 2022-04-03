from setuptools import find_packages, setup

setup(
    name='compare_alt_branches',
    packages=find_packages(include=['compare_alt_branches']),
    version='0.2.0',
    description='',
    author='Morozova E.',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)