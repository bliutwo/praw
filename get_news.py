import get_hot
import threading

l = ['coronavirus', 'news', 'coronavirusca', 'politics', 'worldnews']
threads = []
for s in l:
    t = threading.Thread(target=get_hot.get_hot, args=(s,))
    threads.append(t)
    t.start()
