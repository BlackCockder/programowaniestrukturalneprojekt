import requests

def get_public_ip_address():
    response = requests.get('https://api.ipify.org')
    return response.text

if __name__ == "__main__":
    my_public_ip = get_public_ip_address()
    print("My public IP address is:", my_public_ip)
