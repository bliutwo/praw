from smmryapi import SmmryAPI

def get_summary(url: str, api_key: str, smrry) -> str:
    s = smrry.summarize(url,sm_length=3)
    return s.sm_api_content

if __name__ == "__main__":
    fp = open('api_key.in', 'r')
    api_key = fp.readline().rstrip()
    smmry = SmmryAPI(api_key)
    print(get_summary("https://www.cnbc.com/2020/06/08/asymptomatic-coronavirus-patients-arent-spreading-new-infections-who-says.html", api_key, smmry))
