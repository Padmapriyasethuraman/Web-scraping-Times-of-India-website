#install each package

!pip install requests
!pip install beautifulsoup4
!pip install pandas
!pip install openpyxl

#import the packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

#website URL
url = 'https://timesofindia.indiatimes.com/entertainment/tamil/movie-reviews'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Scraping movie titles, summaries, and ratings
    movies = []
    review_containers = soup.find_all('div', class_='mr_lft_box')

    for container in review_containers:
        title = container.find('h3').get_text().strip()
        summary = container.find('p').get_text().strip()
        
        # Rating
        rating_tag = container.find('span', class_='star_count')
        rating = rating_tag.get_text().strip() if rating_tag else 'N/A'
        
        movies.append({
            'Title': title,
            'Summary': summary,
            'Rating': rating
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(movies)
    
    # Save to Excel
    df.to_excel('tamil_movie_reviews.xlsx', index=False)
    print('Data saved to tamil_movie_reviews.xlsx')
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
