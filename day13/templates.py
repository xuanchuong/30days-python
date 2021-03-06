import os

def get_template_path(path):
    template_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(template_path):
        raise Exception("This is not valid template path %s" %path)
    return template_path

def get_template(path):
    file_template = get_template_path(path)
    return open(file_template).read()

def render_context(template_string, context):
    return template_string.format(**context)