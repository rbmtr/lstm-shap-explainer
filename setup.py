from setuptools import setup, find_packages

with open('requirements.txt') as f:
    REQUIREMENTS = f.read()

setup(
    name='shap_explainer',
    version='0.1',
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True
)
