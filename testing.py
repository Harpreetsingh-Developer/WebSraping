import requests
from bs4 import BeautifulSoup
import csv

# URL of the Dell Service Center page
url = "https://www.dell.com/support/home/en-in/servicecenter"

def scrape_dell_service_centers(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the service center containers
        service_centers = soup.find_all('div', class_='Gcare Service Solutions Private Limitedd')  # Adjusted selector

        data = []
        for center in service_centers:
            name = center.text.strip()  # Extract the name
            address = "Address Placeholder"  # Replace with actual logic to extract address
            contact = "Contact Placeholder"  # Replace with actual logic to extract contact

            # Extract City/Pin Code if available
            city = "City Placeholder"
            pin_code = "Pin Code Placeholder"

            data.append({
                'Name': name,
                'Address': address,
                'Contact': contact,
                'City/Pin Code': f"{city}, {pin_code}"
            })

        # Save data to a CSV fileS
        with open("dell_service_centers.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Address', 'Contact', 'City/Pin Code'])
            writer.writeheader()
            writer.writerows(data)

        print("Data saved successfully to 'dell_service_centers.csv'!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
scrape_dell_service_centers(url)
