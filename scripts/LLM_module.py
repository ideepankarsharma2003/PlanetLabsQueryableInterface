

initial_prompt_for_object_detection= """
You are given with a query and some comma separated object classes. You have to identify the potential classes out of object classes that exist in the given query.
The response should be strictly formatted in following json schema:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "class": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "uniqueItems": true
    }
  },
  "required": ["class"]
}
```
For example:
query: "How many vehicles are there in New York Highway?"
object_classes: "car", "building", "people", "bicycle", "trees", "bus"

Response should be:
```json
{"class": ["car", "bus", "bicycle"]}
```



Using above example, generate response for this:


"""














import requests
url= "https://www.blackbox.ai/api/chat"
import json
from tqdm import tqdm
import re
r= "{[^{]+}"

def input_string_2_json(input_string:str):
    jsn= []
    for question in re.findall(r, input_string):
        # print(question)
        try:
            jsn.append(json.loads(question))
        except:
            pass
        
    return jsn





def find_potential_classes_in_query(user_query:str, 
                                    potential_classes:list):
    formattable_prompt= f"""
        query: {user_query}
        object_classes: {", ".join(potential_classes)}

        Give me formatted json for the potential classes:
        """
        
    prompt= initial_prompt_for_object_detection+formattable_prompt
    response= requests.post(url, json={"messages":[{"id":"OfS3kB7","content":prompt,"role":"user"}],"id":"OfS3k7","previewToken":None,"userId":"0cf5b2a2-04cd-4107-b3d1-935498418149","codeModelMode":True,"agentMode":{},"trendingAgentMode":{},"isMicMode":False,"userSystemPrompt":None,"maxTokens":None,"webSearchMode":True,"promptUrls":None,"isChromeExt":False,"githubToken":None})
    result= (response.content.decode())[0]
    
    
    result= input_string_2_json(result)
    print(f"""   
          {result}
     """)
    return  result
    

