import re
from distutils.core import setup

# Get version this way, so that we don't load any modules.
with open('./workflowmax/__init__.py') as f:
    exec(re.search(r'VERSION = .*', f.read(), re.DOTALL).group())

try:
    setup(
        name='pyworkflowmax',
        packages=['workflowmax'],
        version=__version__,
        description='Python API for accessing the REST API of the WorkflowMax accounting tool.',
        license='BSD',
        author='Jarek Głowacki',
        author_email='jarekwg@gmail.com',
        url='https://github.com/ABASystems/pyworkflowmax',
        keywords=['workflowmax'],
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
        install_requires=[
            'requests>=2.10.0',
        ],
    )
except NameError:
    raise RuntimeError("Unable to determine version.")
