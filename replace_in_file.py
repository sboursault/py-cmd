import re

def process_file(path, regex, replacement, if_content_matches = None, if_content_doesnt_match = None):
    regex_to_satisfy = if_content_matches
    regex_not_to_satisfy = if_content_doesnt_match
    with open(path) as f:
        content = f.read()
        match = re.search(regex, content) is not None and (
            regex_to_satisfy is not None and re.search(regex_to_satisfy, content)
            or regex_not_to_satisfy is not None and not re.search(regex_not_to_satisfy, content)
            or regex_to_satisfy is None and regex_not_to_satisfy is None)
    if match:
        new_content = re.sub(regex, replacement, content)
        with open(path, "w") as f:
            f.write(new_content)
            print(path + " updated")


process_file(
    path = "...",
    regex = r"...",
    replacement = "..."
)
