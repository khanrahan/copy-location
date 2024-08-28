'''
Copy Location

URL:

    http://github.com/khanrahan/copy-location

Description:

    Copy location of item inside of Flame (as opposed to the path in the file system).

Available for the following items:

    Batch Groups
    Batch Iterations
    Clips
    Desktops
    Folders
    Libraries
    Reels
    Reel Groups
    Sequences

Menus:

    Right-click selected items on the Desktop --> Copy... --> Location to Clipboard
    Right-click selected items in the Media Panel --> Copy... --> Location to Clipboard

To Install:

    For all users, copy this file to:
    /opt/Autodesk/shared/python

    For a specific user, copy this file to:
    /opt/Autodesk/user/<user name>/python
'''

import socket
import flame
from PySide2 import QtWidgets

TITLE = 'Copy Location'
VERSION_INFO = (1, 2, 0, 'dev')
VERSION = '.'.join([str(num) for num in VERSION_INFO])
TITLE_VERSION = '{} v{}'.format(TITLE, VERSION)
MESSAGE_PREFIX = '[PYTHON HOOK]'
SEPARATOR = ' > '


def message(string):
    '''Print message to shell window and append global MESSAGE_PREFIX.'''

    print(" ".join([MESSAGE_PREFIX, string]))


def copy_to_clipboard(text):
    '''Self explanitory.  Only takes a string.'''

    qt_app_instance = QtWidgets.QApplication.instance()
    qt_app_instance.clipboard().setText(text)


def get_hostname():
    '''Return hostname without the domain.'''

    hostname = socket.gethostname().split('.')[0]

    return hostname


def find_parents(starting_item):
    '''Returns a list of parent object names ascending from right to left.'''

    current_item = starting_item
    parents = [current_item.name.get_value()]

    while current_item.parent:
        if isinstance(current_item.parent, flame.PyProject):
            parents.insert(0, current_item.parent.name)  # already a string
        else:
            parents.insert(0, current_item.parent.name.get_value())

        current_item = current_item.parent

    parents.insert(0, get_hostname())  # make hostname the root

    return parents


def copy_locations(selection):

    message(TITLE_VERSION)
    message('Script called from {}'.format(__file__))

    paths = []

    for item in selection:
        location_path = SEPARATOR.join(find_parents(item))
        message(location_path)
        paths.append(location_path)

    copy_to_clipboard('\n'.join(paths))

    message('Copied to clipboard!')
    message('Done!')


def scope_item(selection):

    for item in selection:
        if isinstance(item, (flame.PyBatch,
                             flame.PyBatchIteration,
                             flame.PyClip,
                             flame.PyDesktop,
                             flame.PyFolder,
                             flame.PyLibrary,
                             flame.PyReel,
                             flame.PyReelGroup)):
            return True
    return False


def get_media_panel_custom_ui_actions():

    return [{'name': 'Copy...',
             'actions': [{'name': 'Location to Clipboard',
                          'isVisible': scope_item,
                          'execute': copy_locations,
                          'minimumVersion': '2022'}]
            }]
