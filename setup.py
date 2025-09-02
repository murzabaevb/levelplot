from setuptools import setup, find_packages

setup(
    name="levelplot",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=[
        'matplotlib~=3.9.2',
    ],
    author='Bakyt-Bek Murzabaev',
    author_email='b.b.murzabaev@gmail.com',
    description='A Python class for signal level visualizations using Matplotlib.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/murzabaevb/levelplot',
    download_url='https://github.com/murzabaevb/levelplot',
    license='GNU General Public License',
    license_files='https://www.gnu.org/licenses/',
    keywords='spectrum,frequency,plot',
)

