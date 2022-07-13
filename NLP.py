

# Подключение модуля Wikipedia : pip install wikipedia
import wikipedia
# Подключение модуля Spacy : pip install spacy
import spacy  
# Подключение модуля Textacy : pip install textasy
import textacy
# Загрузка английской NLP-модели как модуль, около 400 мб :  python -m spacy download en_core_web_lg
import en_core_web_lg 
# Определяем поисковый аргумент
subject = 'The Great Attractor' 
# Ищем запрос, представленный с помощью аргумента
wikiResults = wikipedia.search(subject) 
wikiPage = wikipedia.page(wikiResults[0]).content
nlp = en_core_web_lg.load()
# Анализ
document = nlp(wikiPage) 
# Создаем пустой список для будущих фактов
uniqueStatements = list() 
# Извлечение полуструктурированных выражений
for word in ["Great", "Attractor", "Great Attractor"]:
    for cue in ["is a", "was", "moving", "be"]:
        statments = textacy.extract.semistructured_statements(doclike=document, entity=word, cue=cue, fragment_len_range=None)
        
        for statement in statments:
            uniqueStatements.append(statement)
# Вывод фактов
print("found", len(uniqueStatements), "statements.")
for statement in uniqueStatements:
    entity, cue, fact = statement
    print(*entity, *cue, *fact) 
