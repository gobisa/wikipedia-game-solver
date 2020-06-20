from bs4 import BeautifulSoup
import requests
from collections import deque

WIKI_BASE_URL = "https://en.wikipedia.org/wiki/"

start_topic = "Counter-Strike"
end_topic = "Microsoft_Windows"

start_link = WIKI_BASE_URL + start_topic
searched_topics = set()
unsearched_topics = deque([start_topic])

while len(unsearched_topics) != 0:
    current_topic = unsearched_topics.popleft()
    searched_topics.add(current_topic)
    current_link = WIKI_BASE_URL + current_topic
    current_page_request = requests.get(current_link)
    #print(current_page_request)
    current_page = current_page_request.content
    print(type(current_page))
    soup = BeautifulSoup(current_page, features="html.parser")

    for a_tag in soup.find_all('a'):
        new_topic = a_tag.get("href")
        wiki_dir = "/wiki/"
        is_wiki_topic = new_topic.startswith(wiki_dir)
        if is_wiki_topic:
            print(new_topic)
            if new_topic == end_topic:
                break
            elif new_topic not in searched_topics:
                unsearched_topics.append(new_topic[len(wiki_dir)])
                #FIXME: keep track of parent to build history

print("found it")

