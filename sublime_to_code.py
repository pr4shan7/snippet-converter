import os
import json
import xml.etree.ElementTree as ET

variables_file = open('variables.json', 'r')
variables = json.load(variables_file)
variables_file.close()


def get_scope(s: str) -> str:
    ret = ''
    for scope in variables['scopes']:
        if scope in s:
            ret += ', ' + \
                variables['scopes'][scope] if len(
                    ret) else variables['scopes'][scope]
    return ret


output = {}
snippets = os.listdir(variables['SUBLIME_SNIPPET_PATH'])
for snippet in snippets:
    tree = ET.parse(variables['SUBLIME_SNIPPET_PATH'] + '/' + snippet)
    root = tree.getroot()
    output[snippet[0:-16]] = {
        'scope': get_scope(root[3].text),
        'prefix': root[1].text,
        'body': root[0].text[1:-1],
        'description': root[2].text
    }

output_file = open(variables['CODE_SNIPPET_PATH'] +
                   '/' + 'sublime_snippets.code-snippets', 'w')
json.dump(output, output_file, ensure_ascii=False, indent=2, sort_keys=True)
output_file.close()
