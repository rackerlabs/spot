import os
import requests

def get_all_droplet_sizes(api_token):
    url = "https://api.digitalocean.com/v2/sizes"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    all_sizes = []
    while True:
        response = requests.get(url, headers=headers, params={"per_page": 100})

        if response.status_code == 200:
            json_response = response.json()
            sizes_on_page = json_response["sizes"]
            all_sizes.extend(sizes_on_page)
            
            if "links" in json_response and "pages" in json_response["links"] and "next" in json_response["links"]["pages"]:
                url = json_response["links"]["pages"]["next"]
            else:
                break
        else:
            print(f"Failed to fetch droplet sizes. Status code: {response.status_code}")
            print(response.text)
            print
            break

    return all_sizes

if __name__ == "__main__":
    api_token = os.getenv('DIGITALOCEAN_API_TOKEN')
    if api_token is None:
        raise ValueError("DigitalOcean API token not set. Please set the DIGITALOCEAN_API_TOKEN environment variable.")


    all_droplet_sizes = get_all_droplet_sizes(api_token)
    for size in all_droplet_sizes:
        print(f"Size: {size['slug']}, Price: ${size['price_hourly']} per hour")
