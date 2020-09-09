import json

with open('newsafr.json') as f:
  data_json = json.load(f)
  news_str = ' '
  for news in data_json['rss']['channel']['items']:
    news_str += news['description']
  list_all_word = news_str.split(' ')
  new_list = []
  for element in list_all_word:
    if len(element) > 6:
      new_list.append(element)
    else:
      continue
  common_words = sorted(set(new_list), key = new_list.count, reverse = True)

print(common_words[:10])