from setuptools import setup, find_packages


setup(
    python_requires='>3.0.0',
    name='dirtree',
    version='0.3dev',
    packages=find_packages(),
    license='MIT',
    description='Generates representations of directory trees.',
    long_description='Shell script that generates representations of \
        directory trees in a variety of formats, such as LaTeX forest.',
    author='Lucas F Torroba Hennigen',
    author_email='lucasfth@gmail.com',
    url='https://github.com/zesme/dirtree',
    entry_points = {
        'console_scripts': ['dirtree=dirtree.__main__:main'],
    },
)
