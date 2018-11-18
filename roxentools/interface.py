# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs *
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def interface_call(username='', password='', url="https://localhost:9999", path="/", sesh=requests.Session(), conf_file='/root/roxentools_conf.json', ):
    """This is an example of a module level function.

    Function parameters should be documented in the ``Args`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    If \*args or \*\*kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name (type): description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        username (str): The Administration User Name.

        password (str): The Administration Password.

        url (:obj:`str`, optional): The second parameter. Defaults to https://localhost:9999.
            This will be required outside of local development.

        \*args: Variable length argument list.

        \*\*kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.

        ValueError: If `param2` is equal to `param1`.

    """
    if (username == '' or password == '') and conf_file:
        try:
            with open(conf_file) as filein:
                conf = json.load(filein)
                username = conf['username']
                password = conf['password']
        except IOError:
            print('username or password not provided or could read file %s', conf_file)
            raise

    if username != '' and password != '':
        request_url = url + path

        
        auth = sesh.get(url + "/", auth=(username, password), verify=False)
        wizardid = sesh.cookies['RoxenHttpsWizardId']
        wizard_url = request_url + "&_roxen_wizard_id=" + wizardid
        response = sesh.get(wizard_url, auth=(username, password), verify=False)

        return response
