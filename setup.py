from setuptools import find_packages, setup

setup (
    name= "mcqgen_demo",
    version='0.0.1',
    author="Raveendra Seetharam",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "pyPDF2"],
    packages=find_packages()
)