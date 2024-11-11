from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Sai',
    author_email='saikrishna.gelli1998@outlook.com',
    install_requires=["openai","azureopenai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages() 
)