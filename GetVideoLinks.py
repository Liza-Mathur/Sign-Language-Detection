import json

def getVideoLinks()-> dict:
    with open('WLASL_v0.3.json',"r") as file:
        data = json.load(file)
    all_urls = {}
    for words in data:
        word = words.get('gloss','NA')
        instances = words.get('instances',[])
        all_urls.update({word : []})
        for i in instances:
            url = i.get('url',None)
            if url:
                all_urls[word].append(url)
    return all_urls

# all_urls = []
# for words in data:
#     word = words.get('gloss','NA')
#     instances = words.get('instances',[])
#     for i in instances:
#         url = i.get('url',None)
#         if url:
#             all_urls.append((word,url))

if __name__ == "__main__":
    all_urls = getVideoLinks()
    urlcounts = {word: len(urls) for word, urls in all_urls.items()}
#  I can do - urlcounts = urlcounts | {word : 1}
    print(urlcounts)
    print('I hope this works')

