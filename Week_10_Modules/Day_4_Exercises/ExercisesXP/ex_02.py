import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

"""
Access the nested “salary” key from the JSON-string above.
Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
Save the dictionary as JSON to a file.
"""


json_dict = json.loads(sampleJson)
print(json_dict['company']['employee']['payable']['salary'])

with open('file.json', mode='w') as f:
    json.dump(json_dict, f, indent=2)