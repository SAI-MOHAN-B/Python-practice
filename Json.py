import json
import logging

person = {"name": "John", "age": 30, "city": "new York"}
person_1 = json.dumps(person)
logging.info(f"{person_1}", person_1)
print(person_1)

# Json to Python dict
person_json = """
{
"age":30,
"city":"New York",
"haschildren": false,
"name": "John"
}
"""
person_data = json.loads(person_json)
print(person_data)
