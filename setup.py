from setuptools import setup

deps = ['numpy', 'scipy', 'scikit-image', 'imageio', 'natsort', 'tqdm']

setup(
    name='cv_gmm_deep',
    version='0.0.1',
    description='Private package for GMM and Deep Learning utilities',
    url='git@github.com:mamello-justice/cv_gmm_deep.git',
    author='Mamello Seboholi',
    author_email='j.seboholi@gmail.com',
    packages=['cv_gmm_deep'],
    install_requires=deps
)
