import sys
import re

def get_platform():
    if sys.platform.startswith('linux'):
        return 'linux'
    elif sys.platform.startswith('win32'):
        return 'win'
    elif sys.platform.startswith('darwin'):
        return 'mac'
    else:
        return sys.platform
    
def split_tag(string:str, delimeters:list[str], tag_exception_list:list[str]) -> list[str]:
    tags = []

    # Add split exception values to tags
    for i in tag_exception_list:
        if i in string:
            tags.append(i)
            string = string.replace(i, '')
    
    _escaped = [re.escape(d) for d in delimeters]
    pattern = '|'.join(_escaped)
    tags.extend(re.split(pattern, string))

    # Remove end spacing and duplicate values
    tags = [i.strip() for i in list(set(tags))]
    tags.remove('')
    return tags

