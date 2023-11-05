# ⚡python-list-based-api-scraper (PAS)
A general tool to iterate over apis that provide a list of endpoints and download what's on that endpoint to a text file.
To give a brief example:

Let's say, `http://apis.com/list` returns a list of all available APIs online.

```json
pokemon, beer, humans, dog+breeds, cockatails
car+brands, names, uniforms, sector
```
and `http://apis.com/pokemon` will return all available pokemon, `/beer` will return all available beer brands and so on.
This code will be able to retrieve the list, split the lines and items based on a defined delimiter. Afterwards
you can use the API defined in this code to call the base url of your choice to retrieve, download and save the output of said endpoint
to a file. 

This was originally made to be able to have a simple way of automating a tedious task. I hope you also
find this code useful. 


### ✨  State
This code is VERY rigid right now. This was only implemented as a helper code for another program I am writing.
to use the code, if your needs are conform the parameters of this project, the only thing
you would need to change are the following parameters at the top of `src/main.py` file:

```python
TIME_DELAY = 1
LIST_URL = "https://www.myapi.com/api/list"
BASE_URL = "https://www.myapi.com/"
SAVE_LOCATION = "./output/"
```


## 🛠️ Improvement plan
The improvement plan for this repo is to turn this codebase into a relatively well structured python package.
- [x] Provide clear support for raw text based lists and endpoints
- [ ] Convert codebase into python package
- [ ] Implement Github Actions for testing
- [ ] Create Release

## 🛣️ Feature Roadmap
- [x] Text Support
- [ ] JSON Support
- [ ] XML  Support

## ⚒️ Built with
- Poetry
- Python 3.12
- Requests