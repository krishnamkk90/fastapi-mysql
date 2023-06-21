from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import mysql.connector
import schedule, time

def scrape_and_store_data():

    # Set the path to the ChromeDriver executable
    chrome_driver_path = '/home/krishna/project/interview-task/scapper/chromedriver'

    # Set up the ChromeDriver service
    chrome_service = Service(chrome_driver_path)

    # Set up the Selenium WebDriver using the ChromeDriver service
    driver = webdriver.Chrome(service=chrome_service)

    # Open the URL in the browser
    driver.get('https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx')

    # Wait for the page to load (adjust the time if needed)
    driver.implicitly_wait(10)

    # Extract the HTML content
    html_content = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table containing the bulk deals data
    table = soup.find('table', {'id': 'ContentPlaceHolder1_gvbulk_deals'})

    # Extract the data from the table
    rows = table.find_all('tr')
    data = []
    for row in rows:
        columns = row.find_all('td')
        if columns:
            deal_date = columns[0].text.strip()
            security_code = columns[1].text.strip()
            security_name = columns[2].text.strip()
            client_name = columns[3].text.strip()
            deal_type = columns[4].text.strip()
            quantity = columns[5].text.strip().replace(',', '')
            price = columns[6].text.strip().replace(',', '')
            # Process and use the extracted data as needed
            print(f"Date: {deal_date}, Security Code: {security_code}, Security Name: {security_name}, Client Name: {client_name}, Deal Type: {deal_type}, Quantity: {quantity}, Price: {price}")
            data.append((deal_date, security_code,security_name, client_name, deal_type, quantity, price))
    cnx = mysql.connector.connect(user='user', password='password', host='localhost', database='user_db')
    cursor = cnx.cursor()
    query = "INSERT INTO scraped_data (deal_date, security_code,security_name, client_name, deal_type, quantity, price) VALUES (STR_TO_DATE(%s, '%d/%m/%Y'), %s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, data)
    cnx.commit()
    cursor.close()
    cnx.close()

def run_scraper_daily():
    scrape_and_store_data()

# Schedule the scraper to run once daily at a specific time (e.g., 2:00 AM)
schedule.every().day.at("02:00").do(run_scraper_daily)

#Schedule the scraper to run every 5minutes this is to test the script
#schedule.every(5).minutes.do(run_scraper_daily)

while True:
    schedule.run_pending()
    time.sleep(1)

