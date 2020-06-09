from smmryapi import SmmryAPI
import sys

def get_summary(url: str, api_key: str, smrry) -> str:
    summary = None
    try:
        s = smrry.summarize(url,sm_length=3)
        summary = s.sm_api_content
    except:
        summary = sys.exc_info()[0]
    return summary


if __name__ == "__main__":
    fp = open('api_key.in', 'r')
    api_key = fp.readline().rstrip()
    smmry = SmmryAPI(api_key)
    print(get_summary("https://www.cnbc.com/2020/06/08/asymptomatic-coronavirus-patients-arent-spreading-new-infections-who-says.html", api_key, smmry))
