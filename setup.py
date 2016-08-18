from distutils.core import setup

setup(
    name='pyworkflowmax',
    packages=['workflowmax'],
    version=__import__('workflowmax').__version__,
    description='Python API for accessing the REST API of the WorkflowMax accounting tool.',
    license='BSD',
    author='Jarek Głowacki',
    author_email='jarekwg@gmail.com',
    url='https://github.com/ABASystems/pyworkflowmax',
    download_url='https://github.com/ABASystems/pyworkflowmax/tarball/0.1',
    keywords=['workflowmax'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Office/Business',
    ],
)
