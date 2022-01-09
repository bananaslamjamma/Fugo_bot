import requests
import json

# testing out the MAL api for use in personal discord project

CLIENT_AUTH = "X-MAL-CLIENT-ID"
TOKEN = "499fee48172343e29aa9cf2578e03770"


def get_search(query):
    print(query)
    # should probably do an exception check if not found
    response = requests.get("""https://api.myanimelist.net/v2/anime?q={}&limit=1""".format(query),
                            headers={CLIENT_AUTH: TOKEN})
    print(response)
    data = response.json()
    #print(json.dumps(data, indent=4, sort_keys= True))
    # dumps the json object into an element
    json_str = json.dumps(data)
    # load the json to a string
    resp_dict = json.loads(json_str)
    #title = resp_dict['data'][0]['node'].get('title')
    id = resp_dict['data'][0]['node'].get('id')
    print(id, " + This is SEARCH")
    return(id)


def get_anime(anime_name):
    id = get_search(anime_name)
    URL =  "https://api.myanimelist.net/v2/anime/{}?fields= id, title, main_picture, alternative_titles, start_date, end_date, synopsis, mean, rank, popularity".format(id)
   # """https: // api.myanimelist.net/v2/anime/{}?fields=id,title, main_picture, alternative_titles, start_date, end_date, synopsis, mean, rank, popularity, num_list_users, num_scoring_users, nsfw,created_at, updated_at, media_type"""
    response = requests.get(URL, headers={CLIENT_AUTH: TOKEN})
    print(response)
    data = response.json()
    print("THIS IS ANIME")
    print(json.dumps(data, indent=4, sort_keys=True))
    json_str = json.dumps(data)
    # load the json to a string
    resp_dict = json.loads(json_str)
    title = resp_dict.get('title')
    print(title)

    # TODO should print a discord title box with detailed info
    return


def get_mal():
    response = requests.get("https://api.myanimelist.net/v2/anime/10357?fields=rank,mean,alternative_titles",
                            headers={CLIENT_AUTH: TOKEN})
    print(response)

    data = response.json()
    #print(json.dumps(data, indent=4, sort_keys= True))

    id = data['id']
    title = data['title']

    print(title)
    print(id)
    return(title)


get_mal()
get_anime("Mobile Suit Gundam Seed")
