import webbrowser
import pyperclip
import sys

arguments = sys.argv
maps_api = "https://www.google.com/maps/search/"
address = arguments.pop() if len(arguments) > 1 else pyperclip.paste()

webbrowser.open(maps_api + "+".join(address.split()))