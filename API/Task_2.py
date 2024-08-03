import requests


def check_sites_status(list_of_urls):
    for url in list_of_urls[:-1]:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Status code of url: {response.url}\n is GOOD!")
        else:
            print(f"Status code of url: {response.url}\n is {response.status_code}!")
        print("----------")


urls = list()
variable = "x"
while variable.upper() != "Y":
    variable = input("Enter the site URL for connection check (or 'y' if is all'): ")
    urls.append(variable)
check_sites_status(urls)
