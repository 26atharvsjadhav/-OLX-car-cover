from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

def scrape_olx_car_cover():
    url = "https://www.olx.in/items/q-car-cover"
    
    options = Options()
    options.headless = True  # Run Chrome in headless mode (no browser window)
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    time.sleep(5)  # Wait for page to load (adjust if needed)
    
    ads = driver.find_elements(By.CSS_SELECTOR, "li.EIR5N")  # Each listing container
    
    results = []
    for ad in ads:
        try:
            title = ad.find_element(By.CSS_SELECTOR, "span._2tW1I").text
            price = ad.find_element(By.CSS_SELECTOR, "span._89yzn").text
            location = ad.find_element(By.CSS_SELECTOR, "span.CFYHk").text
            link = ad.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            results.append({
                "title": title,
                "price": price,
                "location": location,
                "link": link
            })
        except Exception:
            # Skip listings missing some info
            continue
    
    driver.quit()
    
    # Save results to CSV file
    with open("olx_car_cover_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "location", "link"])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"Saved {len(results)} results to olx_car_cover_results.csv")

if __name__ == "__main__":
    scrape_olx_car_cover()
