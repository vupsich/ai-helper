from rdflib import Graph
from ontology_utils import extract_and_save_classes

g = Graph()
g.parse("schemaorg.owl", format="xml")

file_path = extract_and_save_classes(g)
print(f"Список классов сохранён в файл: {file_path}")