from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = ''.join(f.readlines())

install_requires = []

with open('requirements.txt') as f:
    for line in f.readlines():
        req = line.strip()
        if not req or req.startswith(('-e', '#')):
            continue
        install_requires.append(req)

setup(
    name='vocloud-authenticator',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/kozajaku/vocloud-authenticator',
    license='MIT',
    author='kozajaku',
    author_email='kozajaku@fit.cvut.cz',
    description='JupyterHub to Vocloud authentication module',
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=['vocloud', 'jupyter', 'jupyterhub'],
    install_requires=install_requires,
)
