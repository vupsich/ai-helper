import os
from rdflib.namespace import RDFS

def extract_and_save_classes(graph, file_name="classes.txt"):
    # Список для хранения классов
    classes = []

    # Извлекаем классы из онтологии
    for subject, predicate, obj in graph.triples((None, RDFS.subClassOf, None)):
        classes.append(str(subject))  # Преобразуем URI в строку

    # Сортируем список классов
    sorted_classes = sorted(classes)

    # Определяем путь для сохранения файла
    work_dir = os.getcwd()
    file_path = os.path.join(work_dir, file_name)

    # Записываем отсортированный список в файл
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(sorted_classes))

    return file_path