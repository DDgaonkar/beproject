import requests 
import bs4
res = requests.get('https://www.amazon.in/Power-Your-Subconscious-Mind-Success/dp/8172345666/ref=sr_1_1_sspa?s=books&ie=UTF8&qid=1536939154&sr=1-1-spons&keywords=books&psc=1&smid=A05378423NJE7Q5XCN3XZ')

SOUP = bs4.BeautifulSoup(res.text, 'lxml')
