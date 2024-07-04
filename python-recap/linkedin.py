import requests
from bs4 import BeautifulSoup


def scrape_linkedin_profile(profile_url):
    try:
        # Send an HTTP request to the LinkedIn profile
        response = requests.get(profile_url)
        if response.status_code != 200:
            print(f"Error: Failed to retrieve page with status code {response.status_code}")
            return

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract relevant information
        first_name_element = soup.find('li', {'class': 'inline t-24 t-black t-normal break-words'})
        first_name = first_name_element.text.strip() if first_name_element else 'N/A'

        last_name_element = first_name_element.find_next('li') if first_name_element else None
        last_name = last_name_element.text.strip() if last_name_element else 'N/A'

        # Print the extracted data
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    profile_url = "https://www.linkedin.com/in/nayeemh101/"
    scrape_linkedin_profile(profile_url)
