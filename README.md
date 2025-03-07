# Copy Location

Plugin for [Autodesk Flame software](http://www.autodesk.com/products/flame).

Copy location of selected items inside of Flame.

Available for the following items:
 - Batch Groups
 - Batch Iterations
 - Clips
 - Desktops
 - Folders
 - Libraries
 - Reels
 - Reel Groups
 - Sequences
 - Workspaces

## Example
For a single frame of Black on the Desktop, the below would be sent to the clipboard:

`hostname > project_name > WORKSPACE > Desktop > Reels > Reel 1 > BLACK`

## Compatibility
|Release Version|Flame Version|
|---|---|
|v3.X.X|Flame 2025 and up|
|v2.X.X|Flame 2022 up to 2024.2|
|v1.X.X|Flame 2021 up to 2021.2|

## Installation

### Flame 2025 and newer
To make available to all users on the workstation, copy `copy_location.py` to `/opt/Autodesk/shared/python/`

For specific users, copy `copy_location.py` to the appropriate path below...
|Platform|Path|
|---|---|
|Linux|`/home/<user_name>/flame/python/`|
|Mac|`/Users/<user_name>/Library/Preferences/Autodesk/flame/python/`|

### Flame 2023.3.2 up to 2024.2
To make available to all users on the workstation, copy `copy_location.py` to `/opt/Autodesk/shared/python/`

For specific users, copy `copy_location.py` to `/opt/Autodesk/user/<user name>/python/`

### Last Step
Finally, inside of Flame, go to Flame (fish) menu `->` Python `->` Rescan Python Hooks

## Menus
- Right-click selected items on the Desktop `->` Copy... `->` Location to Clipboard
- Right-click selected items in the Media Panel `->` Copy... `->` Location to Clipboard

## Acknowledgements
Many thanks to [pyflame.com](http://www.pyflame.com)
