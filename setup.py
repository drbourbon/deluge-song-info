import setuptools

setuptools.setup(name='deluge-song-info',
    version='0.9.0',
    description='Tool for getting info from Synthstrom Audible Deluge songs',
    author='Fabio Barbon',
    license='MIT',
    scripts=['bin/deluge-song-info'],
    packages=setuptools.find_packages(),
    install_requires=[
        'attrs',
        'audioread',
        'pydel',
    ])