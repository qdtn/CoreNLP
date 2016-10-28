from distutils.core import setup

setup(
    name='CoreNLP',
    version='1.0',
    packages=['liir', 'liir.nlp', 'liir.nlp.io', 'liir.nlp.we', 'liir.nlp.features', 'liir.nlp.representation'
              ],

    includes = ['liir', 'liir.nlp', 'liir.nlp.io', 'liir.nlp.we', 'liir.nlp.features', 'liir.nlp.representation'
              ],

    url='',
    license='',
    author='quynhdo',
    author_email='quynhdtn.hut@gmail.com',
    description=''
)
