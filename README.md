# Roxen Tools

A python package containing tools for managing a roxen web server via python

compatible with python 2.6, 2.7 and 3.6

## Installation

pip install roxentools

## Usage

TODO: 
* create documentation
* use tox and run the tests against different versions of Python
* connect to travis
* sort/confirm requirement for yum installed lxml on centos
* try urlparse in config module

## Development

mkvirtualenv --python=`which python3` roxentools

pip install -e roxentools

pip install -r  requirements_dev.txt

## Testing

pip install roxentools

pip install -r requirements_dev.txt

### tests with coverage

nosetests --with-xunit --with-coverage --cover-xml --cover-html-dir=coverage --cover-html -w tests/ --cover-package=roxentools

### compatibility tests

tox


## Documentation

cd docs

make html

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

initial code base for use imported into python scripts

## Credits

dhunter@digitalcreation.co.nz

## License

see the LICENCE file