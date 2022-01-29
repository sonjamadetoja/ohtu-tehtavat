from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        test_name = parsed["tool"]["poetry"]["name"]
        test_description = parsed["tool"]["poetry"]["description"]
        dependencies_list = list(parsed["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies_list = list(parsed["tool"]["poetry"]["dev-dependencies"].keys())
        return Project(test_name, test_description, dependencies_list, dev_dependencies_list)
