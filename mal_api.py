import requests
import json
import difflib
import re

# testing out the MAL api for use in personal discord project

CLIENT_AUTH = "X-MAL-CLIENT-ID"
TOKEN = "499fee48172343e29aa9cf2578e03770"
LIMIT = 10

def get_search(query):
    try:
        response = requests.get("""https://api.myanimelist.net/v2/anime?q={}&limit={}""".format(query, LIMIT),
                                headers={CLIENT_AUTH: TOKEN})
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4, sort_keys= True))
            # dumps the json object into an element
            json_str = json.dumps(data)
            # load the json to a string
            resp_dict = json.loads(json_str)
            anime_object = resp_dict['data']
            title_list = []
            for x in anime_object:
                #append entries to list
                title_list.append(x['node'].get('title'))
                #print(x['node'].get('title'))                         
            #debug: full query list    
            #print(title_list)
            
            #handy library to find closest match  
            search_list = difflib.get_close_matches(query, title_list)
            #print(search_list)
            #closest match is the first in the list, if fails, select first entry
            try:  
                index = title_list.index(search_list[0])
            except Exception as e:
                print(e)
                index = 0
                
            #print(index, "This is index list")
            id = resp_dict['data'][index]['node'].get('id')

            return(id)
        else:
            print("Not found")
            return
    except Exception as e:
        print(e)
        return


def get_anime(anime_name):
    try:
        id = get_search(anime_name)
        URL = "https://api.myanimelist.net/v2/anime/{}?fields= id, title, main_picture, alternative_titles, start_date, end_date, synopsis, mean, rank, popularity".format(
            id)
    # """https: // api.myanimelist.net/v2/anime/{}?fields=id,title, main_picture, alternative_titles, start_date, end_date, synopsis, mean, rank, popularity, num_list_users, num_scoring_users, nsfw,created_at, updated_at, media_type"""
        response = requests.get(URL, headers={CLIENT_AUTH: TOKEN})
        if response.status_code == 200:
            print(response)
            data = response.json()
            print("THIS IS ANIME")
            #print(json.dumps(data, indent=4, sort_keys=True))
            json_str = json.dumps(data)
            # load the json to a string
            resp_dict = json.loads(json_str)
            title = resp_dict.get('title')
            synopsis = resp_dict.get('synopsis')
            print(title)
            print(synopsis)
            print(id)
            
        else:
            print("cannot retrieve anime info")
            return
    except Exception as e:
        print(e)
        return


def get_mal():
    response = requests.get("https://api.myanimelist.net/v2/anime/10357?fields=rank,mean,alternative_titles",
                            headers={CLIENT_AUTH: TOKEN})
    # print(response)

    data = response.json()
    #print(json.dumps(data, indent=4, sort_keys= True))

    id = data['id']
    title = data['title']

    # print(title)
    # print(id)
    return(title)


#get_mal()
get_anime("Fate/Zero")

msg = "{{guns}}"

def hasBrackets(str):
    matched = re.match('{{2}.{1,}\}{2}', str)
    return bool(matched)

print(msg)
print(hasBrackets(msg))
