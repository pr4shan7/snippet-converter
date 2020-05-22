import os
import json

variables = {}
variables['SUBLIME_SNIPPET_PATH'] = os.path.expanduser(
    '~') + '/.config/sublime-text-3/Packages/User/Snippets'
variables['CODE_SNIPPET_PATH'] = os.path.expanduser(
    '~') + '/.config/Code/User/snippets'
variables['scopes'] = {
    'source.c++': 'cpp',
    'source.python': 'python',
    'source.java': 'java'
}

variables_file = open('variables.json', 'w')
json.dump(variables, variables_file, indent=2)
variables_file.close()
