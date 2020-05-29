import setuptools

setuptools.setup(name='deluge-song-info',
    version='0.1.0',
    description='Tool for getting info from Synthstrom Audible Deluge songs',
    author='Fabio Barbon',
    license='MIT',
    scripts=['bin/deluge-song-info'],
    packages=setuptools.find_packages(),
    install_requires=[
        'attrs',
        'pydel',
    ])