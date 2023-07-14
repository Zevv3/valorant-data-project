import requests
import certifi
import urllib3

http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)


# url = 'https://api.henrikdev.xyz'
puuid = "9d27c934-4228-54c6-bdb2-ec4d3070ee4b"
region = 'na'
affinity = 'na'
shard = 'na'
# match_history = requests.get(f"{url}/valorant/v1/by-puuid/lifetime/matches/{affinity}/{puuid}")
# mmr_change_history = requests.get(f"{url}/valorant/v1/by-puuid/lifetime/mmr-history/{region}/{puuid}")
lockfile_password = 'HL2-Uexneg1SpCwBer4RNg'
port = '58558'
entitlement_token = "eyJraWQiOiJrMSIsImFsZyI6IlJTMjU2In0.eyJlbnRpdGxlbWVudHMiOlsidXJuOmVudGl0bGVtZW50Omdsb2JhbHJpb3QubWVyY2gubG9yYmV0YWphY2tldCIsInVybjplbnRpdGxlbWVudDp2YWxvcmFudHJpb3QudmFsb3JhbnQucGJlIl0sImF0X2hhc2giOiJEb2UxYVVUR1M5MGI5QVZCR2NPWUZRIiwic3ViIjoiOWQyN2M5MzQtNDIyOC01NGM2LWJkYjItZWM0ZDMwNzBlZTRiIiwiaXNzIjoiaHR0cHM6XC9cL2VudGl0bGVtZW50cy5hdXRoLnJpb3RnYW1lcy5jb20iLCJpYXQiOjE2ODkyODAwMTUsImp0aSI6IjkxZXhBQ01rVGdnIn0.AwOa-nxMSevpu-voTAHHg4-ri8x0CSv7CA6aYqthoTwMpgqbGVv_XmikTmrxRC3iBy4eO8o7QseukjA6p3mQySlyyU3lw39PuIABlZ1G6sBhkrVxvlc7w93rp2qFs9fs3x00nA5M9xE1oHx100Mpp1-Rz_rSdGCBPdGdHquUv4UcqNuArVCp2E33HlDavsX5I8Cta4b54cf0PS565BBoefoP0YIb17qmbuyPW3BtZ0hiwkDEgCLmZKOu_StgauNSVkHKxDbBgm-0FbdsS16-S9s_RDKU7hR8Ae9WHEQIG57_pjCNa9zvcUGK8p97wVJPCLKpyz1_P_QaQXpjnEQ0sg"
client_platform = 'ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9'
client_version = 'release-07.01-17-917901'
auth_token = 'eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJwcCI6eyJjIjoiYW0ifSwic3ViIjoiOWQyN2M5MzQtNDIyOC01NGM2LWJkYjItZWM0ZDMwNzBlZTRiIiwic2NwIjpbImFjY291bnQiLCJvcGVuaWQiXSwiY2xtIjpbImZlZGVyYXRlZF9pZGVudGl0eV9wcm92aWRlcnMiLCJlbWFpbF92ZXJpZmllZCIsIm9wZW5pZCIsInB3IiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIiwiYWNjdF9nbnQiLCJsb2NhbGUiLCJyZ25fTkExIiwiYWNjdCIsImFnZSIsImFjY291bnRfdmVyaWZpZWQiLCJhZmZpbml0eSJdLCJkYXQiOnsicCI6bnVsbCwiciI6Ik5BMSIsImMiOiJ1ZTEiLCJ1IjozOTMxNjMxNCwibGlkIjoiWnZMR2RiRUx6OTlmWEpZU19kTDRqZyJ9LCJpc3MiOiJodHRwczpcL1wvYXV0aC5yaW90Z2FtZXMuY29tIiwiZXhwIjoxNjg5MjgzMTkyLCJpYXQiOjE2ODkyNzk1OTIsImp0aSI6IjkxZXhBQ01rVGdnIiwiY2lkIjoicGxheS12YWxvcmFudC13ZWItcHJvZCJ9.PxKJ1vfJpAmR660gw-qEpSH8OgFVARgkwZEWM4sIpq7FXGeqOprt6aU9JOekjsxOXGse91U2YcLbMhW3MDa8Yc10NwajWxCzJK7HkLzjtf3QRCpxHZm5va29Jx7I__9Ws9sLQYXzP6_qYWhTtSXXIeyUFgc3qpQJJRDuQSq1z1w'
headers = {
    'X-Riot-Entitlements-JWT': f'{entitlement_token}',
    'Authorization': f'Bearer {auth_token}',
    'X-Riot-ClientPlatform': f'{client_platform}',
    'X-Riot-ClientVersion': f"{client_version}"
}
first_20 = requests.get(f"https://pd.na.a.pvp.net/match-history/v1/history/{puuid}?startIndex=0&endIndex=20&queue=competitive", headers=headers)
second_20 = requests.get(f"https://pd.na.a.pvp.net/match-history/v1/history/{puuid}?startIndex=21&endIndex=40&queue=competitive", headers=headers)
first_20 = first_20.json()
second_20 = second_20.json()
match_IDs = []
# print(first_20)
history = first_20['History'] + second_20['History']
for match in history:
    match_IDs.append(match['MatchID'])

stats_history = []
ranks = {
    1: 'iron I',
    2: 'iron II',
    3: 'iron III',
    4: 'bronze I',
    5: 'bronze II',
    6: 'bronze III',
    7: 'silver I',
    8: 'silver II',
    9: 'silver III',
    10: 'gold I',
    11: 'gold II',
    12: 'gold III',
    13: 'plat I',
    14: 'plat II',
    15: 'plat III',
    16: 'diamond I',
    17: 'diamond II',
    18: 'diamond III',
    19: 'ascendant I',
    20: 'ascendant II',
    21: 'ascendant III',
    22: 'immortal I',
    23: 'immortal II',
    24: 'immortal III',
    25: 'radiant'
}

for id in match_IDs:
    stats = requests.get(f"https://pd.na.a.pvp.net/match-details/v1/matches/{id}", headers=headers)
    stats = stats.json()
    my_stats = {}
    rounds = []
    team = ''
    for player in stats['players']:
        if player['subject'] == puuid:
            my_stats = player["stats"]
            team = player['teamId']
            rounds = player['roundDamage']
            rank = ranks[player['competitiveTier']]

    stats_history.append(my_stats)

class Match():
    def __init__(self, stats, my_stats, rounds, rank, win):
        self.stats = stats
        self.my_stats = my_stats
        self.rounds = rounds 
        self.rank = rank
        self.win = win


print(f"history: {stats_history}")