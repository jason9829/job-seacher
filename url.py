import urllib
from urllib.parse import urlparse
from urllib.parse import parse_qs  # Got error so import like this

QUERY_LOCATION_NUMBER_PARSED = 4
# Desc: Change the value in url query
# Param: Url, query, new query value
# Retval: Url with new query value
# Ref:
# 1. https://stackoverflow.com/a/26222204
def changeUrlQueryValue(url, query, newQueryValue):
    parsedItem = urlparse(url)  # Parsed the url into items
    queryDict = parse_qs(parsedItem.query)  # Get the query element in dict
    queryDict[query] = newQueryValue  # Replace the value in 'query' with 'newQueryValue'
    newParsedItem = list(parsedItem)  # Create a new parsed item
    newParsedItem[QUERY_LOCATION_NUMBER_PARSED] = urllib.parse.urlencode(queryDict)  # Encode the query element
    newUrl = urllib.parse.urlunparse(newParsedItem)  # Unparsed the new parsed item
    newUrl = urllib.parse.unquote(newUrl)  # Decode to normal url
    newUrl = newUrl.replace("['", '').replace("']", '')    # Remove "['" and "']"
    return newUrl
