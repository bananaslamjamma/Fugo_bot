import requests

# testing out the MAL api for use in personal discord project


def get_mal():
    response = requests.get("https://api.myanimelist.net/v2/anime/10357?fields=rank,mean,alternative_titles", headers={"X-MAL-CLIENT-ID": "499fee48172343e29aa9cf2578e03770"})
    print(response)

    data = response.json()

    id = data['id']
    title = data['title']

    print(title)
    print(id)
    return(title)


get_mal()