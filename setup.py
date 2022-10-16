from setuptools import setup

setup(
    name='sourceparser',
    version='0.1.0',    
    description='A simple resume parser used for extracting information from resumes',
    url='https://github.com/gamingflexer/resume-parser-ranker',
    author='gamingflexer',
    author_email='',
    license='MIT',
    packages=['sourceparser'],
    install_requires=['spacy>=2.0.0',],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)