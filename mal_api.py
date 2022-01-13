import requests
import json
import difflib
import re

# testing out the MAL api for use in personal discord project

CLIENT_AUTH = "X-MAL-CLIENT-ID"
TOKEN = "499fee48172343e29aa9cf2578e03770"
LIMIT = 10
PATH_PARAMETERS = "id, title, main_picture, alternative_titles, start_date, end_date, synopsis, mean, rank, popularity, status,"

def get_search(query, type):
    try:
        if type == "anime":
            response = requests.get("""https://api.myanimelist.net/v2/anime?q={}&limit={}""".format(query, LIMIT),
                                headers={CLIENT_AUTH: TOKEN})
        elif type == "manga":
            response = requests.get("""https://api.myanimelist.net/v2/manga?q={}&limit={}""".format(query, LIMIT),
                                headers={CLIENT_AUTH: TOKEN})           
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4, sort_keys= True))
            # dumps the json object into an element
            json_str = json.dumps(data)
            # load the json to a string
            resp_dict = json.loads(json_str)
            mal_object = resp_dict['data']
            title_list = []
            for x in mal_object:
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
    


            


def get_mal_object(name, type):
    try:
        id = get_search(name, type)
        if type == "anime":            
             URL = "https://api.myanimelist.net/v2/anime/{}?fields= num_episodes, ".format(
                 id) + PATH_PARAMETERS
        elif type == "manga":
             URL = "https://api.myanimelist.net/v2/manga/{}?fields= num_chapters, ".format(
                 id) + PATH_PARAMETERS
            
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
            main_picture = resp_dict.get('main_picture')['medium']
            start_date = resp_dict.get('start_date')
            end_date = resp_dict.get('end_date')
            popularity  = resp_dict.get('popularity')
            rank = resp_dict.get('rank')
            status = resp_dict.get('status')
            
            #determine type
            if type == "manga":
                num_of = resp_dict.get('num_chapters')            
            elif type == "anime":
                num_of = resp_dict.get('num_episodes')   
                
            return title, synopsis, id, main_picture, start_date, end_date, popularity, rank, status, num_of
            
        else:
            print("cannot retrieve query info")
            return
    except Exception as e:
        print(e)
        return