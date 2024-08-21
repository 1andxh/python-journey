# import request module from urllib
from urllib import request

sample_url = "https://www.google.com/search?q=python%20web%20scraping%20tutorial"
# request the page
page = request.urlopen(sample_url)

# response code
status = page.code
# data type
print(type(page))
print(status)