import os
from rdflib.namespace import RDFS

def extract_and_save_classes(graph, file_name="classes.txt"):
    
    classes = []

    for subject, predicate, obj in graph.triples((None, RDFS.subClassOf, None)):
        classes.append(str(subject))  

    sorted_classes = sorted(classes)

    work_dir = os.getcwd()
    file_path = os.path.join(work_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(sorted_classes))

    return file_path