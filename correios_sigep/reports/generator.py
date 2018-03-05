from jinja2 import Environment, PackageLoader, select_autoescape

class Generator:
    def __init__(self, folder='templates'):
        self._env = Environment(
            loader=PackageLoader('correios_sigep', folder),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def render(self, file_name, **params):
        tpl = self._env.get_template(file_name)
        return tpl.render(**params)