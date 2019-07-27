#!/usr/bin/env python3

# usage: python set_colors.py [toolsPath] [theme file]

import os
import json
import sys
from xml.dom import minidom
from shutil import copyfile

def set_color(xmldoc, cat, name, color):
    found = False
    for category_tag in xmldoc.getElementsByTagName("CATEGORY"):
        if category_tag.getAttribute("NAME") == category:
            found = True
            break

    if not found:
        options_tag = xmldoc.getElementsByTagName("OPTIONS")[0]
        category_tag = xmldoc.createElement("CATEGORY")
        category_tag.setAttribute("NAME", category)
        options_tag.appendChild(category_tag)

    wrapper = xmldoc.createElement("WRAPPED_OPTION")
    wrapper.setAttribute("NAME", name)
    wrapper.setAttribute("CLASS", "ghidra.framework.options.WrappedColor")

    state = xmldoc.createElement("STATE")
    state.setAttribute("NAME", "color")
    state.setAttribute("TYPE", "int")
    state.setAttribute("VALUE", str(color))

    category_tag.appendChild(wrapper)
    wrapper.appendChild(state)

if __name__ == "__main__":
    toolsDir = sys.argv[1]
    themeName = sys.argv[2]

    xmldoc = minidom.parse(os.path.join(toolsDir, "_code_browser.tcd"))

    theme = json.loads(open(themeName, "r").read())

    for tag in xmldoc.getElementsByTagName("WRAPPED_OPTION"):
        if tag.getAttribute("CLASS") == "ghidra.framework.options.WrappedColor":
            tag.parentNode.removeChild(tag)

    for category, colors in theme.items():
        for name, color in colors.items():
            set_color(xmldoc, category, name, color)

    tool = xmldoc.getElementsByTagName("TOOL")[0]
    tool.setAttribute("TOOL_NAME", "CodeBrowser%s" % themeName)

    dragon_path = os.path.join(toolsDir, "black_dragon.png")
    icon = xmldoc.getElementsByTagName("ICON")[0]
    icon.setAttribute("LOCATION", dragon_path)
    copyfile("black_dragon.png", dragon_path)
    print("-> black dragon icon to %s" % dragon_path)

    fileName = os.path.join(toolsDir, "_code_browser_%s.tcd" % themeName)
    open(fileName, "w+").write(xmldoc.toprettyxml(indent="    ", newl="\n"))