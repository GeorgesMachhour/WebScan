import requests
import socket
import subprocess

API_KEY = '8aa9103179c34c319a6b2034a25f2df6'

def fetch_ip_address(website_url):
    try:
        ip_address = socket.gethostbyname(website_url)
        return ip_address
    except socket.gaierror as e:
        print("Error fetching IP address:", e)
        return None

def get_location(ip_address):
    try:
        url = f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip_address}"
        response = requests.get(url)
        data = response.json()
        
        city = data.get('city')
        country = data.get('country_name')
        if city and country:
            return f"{city}, {country}"
        else:
            return None
    except Exception as e:
        print("Error fetching location:", e)
        return None

def domain_scanner(domain_name, sub_domnames):
    print('-----------Scanner Started-----------')
    print('----URL after scanning subdomains----')
    
    for subdomain in sub_domnames:
        url = f"https://{subdomain}.{domain_name}"
        try:
            requests.get(url)
            print(f'[+] {url}')
        except requests.ConnectionError:
            pass
    print('\n')
    print('----Scanning Finished----')
    print('-----Scanner Stopped-----')

def scan_website():
    website_url = input("Enter the website URL: ")
    ip_address = fetch_ip_address(website_url)
    if not ip_address:
        print("Unable to fetch IP address. Exiting.")
        return

    print(f"IP address: {ip_address}")

    location = get_location(ip_address)
    print(f"Location: {location}")

    with open('subdomain_names1.txt', 'r') as file:
        sub_dom = file.read().splitlines()

    domain_scanner(website_url, sub_dom)

if __name__ == "__main__":
    scan_website()
