import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Create Soup
movie_req = requests.get(URL)
movie_html = movie_req.text
soup = BeautifulSoup(movie_html, 'html.parser')
title = soup.findAll('h3', class_ = 'title')
dates = soup.select('p strong')

# print(soup.prettify())

# Extract titles and put them into list
title_text = [" ".join(title_lines.getText().split()[1:]) for title_lines in title]
dates = [dates.getText() for dates in dates]
dates.reverse()
# print(dates)
title_text.reverse()
# print(len(dates))

# Write list to file
title_index = 1
with open("top100movie.txt", 'w') as file:
    for title in title_text:
        file.write(f'{title_index}. {title}\n')
        title_index += 1


