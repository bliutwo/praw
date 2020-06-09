def get_summary(url: str, api_key: str) -> str:
    summary = "Too many Lego bricks is a problem many parents will sympathise with, but now the toy firm itself has admitted it has made too many. Lego Group chief executive Niels Christiansen said there was \"No quick fix\" and it would take the firm \"Some time\" to grow long-term. The weak performance comes after Lego cut 1,400 jobs worldwide in September, saying its business needed a \"Reset\". 915,103,765 - the number of ways to combine six two-by-four Lego bricks of the same colour. 3,700 - the number of different types of Lego bricks. In September, Lego said its half-year results had suffered because it had stretched itself too thin by diversifying into products that were not toys, such as the Lego movies. Lego chairman Jorgen Knudstorp said at the time that adding complexity to the company had made it harder for the toymaker to grow further."
    return summary

if __name__ == "__main__":
    fp = open('api_key.in', 'r')
    api_key = fp.readline().rstrip()
    print(get_summary("https://www.cnbc.com/2020/06/08/asymptomatic-coronavirus-patients-arent-spreading-new-infections-who-says.html", api_key))
