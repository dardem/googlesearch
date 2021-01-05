# googlesearch
googlesearch is a Python library for searching Google, easily. googlesearch uses requests and BeautifulSoup4 to scrape Google. 

## Installation
To install, run the following command:
```bash
python3 -m pip install googlesearch-python
```

## usage
To get results for a search term, simply use the search function in googlesearch. For example, to get results for "Google" in Google, just run the following program:
```python
from googlesearch import search
search("Google")
```

## Additional options
googlesearch supports a few additional options. By default, googlesearch returns 10 results. This can be changed. To get a 100 results on Google for example, run the following program.
```python
from googlesearch import search
search("Google", num_results=100)
```
You can change the language google searches in. For example, to get results in French run the following program:
```python
from googlesearch import search
search("Google", lang="fr")
```
Also, you can specify the date range of search: from which date and to which date you want your returned results be published (or only one of this borders):
```python
from googlesearch import search
search("Google", date_to='1/1/2018', date_from='1/1/2019')
```