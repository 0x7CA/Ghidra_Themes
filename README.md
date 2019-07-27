![ghidra_darknight](/black_dragon.png?raw=true)
 Themes for [Ghidra](https://github.com/NationalSecurityAgency/ghidra)
==============================================================================
Script to write colour schemes to Ghidra installations. Currently limited to Listing and Decompiler view.

There are still some "bugs" in the display, because actually we can't
configure colors for everything:
 * colors in the Symbol Tree window (function names are hard to read)
 * background decompilation window when the cursor is in an undefined function
 * selection in decompilation mode
 * PCode
 * graph window
---
## Themes
* Darknight
![ghidra_darknight](/darknight.png?raw=true)
* Darcula
![ghidra_darcula](/darcula.png?raw=true)

---
## Installation
To install the theme, run the script :

    ./set_colors.py [ghidra tools folder] [theme]
e.g. ./set_colors.py ~/.ghidra/.ghidra-9.0.4/tools/ darcula