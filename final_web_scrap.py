import requests
from bs4 import BeautifulSoup
import multiprocessing
import sys

def scrape_website(url):
    # Step 1: Get the HTML
    r = requests.get(url)
    htmlContent = r.content

    # Step 2: Parse the HTML
    soup = BeautifulSoup(htmlContent, 'html.parser')

    # Step 3: HTML Tree traversal
    # 
    # Commonly used types of objects:
    title = soup.title
    print(type(title)) # 1. Tag
    print(type(title.string)) # 2. NavigableString
    print(type(soup)) # 3. BeautifulSoup
    # # 4. Comment2
    markup = "<p><!-- this is a comment --></p>"
    soup2 = BeautifulSoup(markup)
    print(type(soup2.p.string))

    # Get the title of the HTML page
    title = soup.title

    # Get all the paragraphs from the page
    paras = soup.find_all('p')
    print(paras)
    anchors = soup.find_all('a')

    print(anchors)

    # Get first element in the HTML page
    print(soup.find('p') ) 

    # find all the elements with class lead
    print(soup.find_all("p", class_="lead"))

    # Get the text from the tags/soup
    print(soup.find('p').get_text())
    print(soup.get_text())

    # Get all the anchor tags from the page
    all_links = set()

    # Get all the links on the page:
    for link in anchors:
        if(link.get('href') != '#'): 
            linkText = link.get('href')
            all_links.add(link)
            print(linkText)

def distribute_scraping(urls):
    with multiprocessing.Pool() as pool:
        pool.map(scrape_website, urls)

if __name__ == '__main__':
 import requests
from bs4 import BeautifulSoup
import multiprocessing

def scrape_website(url):
    # Step 1: Get the HTML
    r = requests.get(url)
    htmlContent = r.content

    # Step 2: Parse the HTML
    soup = BeautifulSoup(htmlContent, 'html.parser')

    # Step 3: HTML Tree traversal
    # 
    # Commonly used types of objects:
    title = soup.title
    print(type(title)) # 1. Tag
    print(type(title.string)) # 2. NavigableString
    print(type(soup)) # 3. BeautifulSoup
    # # 4. Comment
    markup = "<p><!-- this is a comment --></p>"
    soup2 = BeautifulSoup(markup)
    print(type(soup2.p.string))

    # Get the title of the HTML page
    title = soup.title

    # Get all the paragraphs from the page
    paras = soup.find_all('p')
    print(paras)
    anchors = soup.find_all('a')

    print(anchors)

    # Get first element in the HTML page
    print(soup.find('p') ) 

    # find all the elements with class lead
    print(soup.find_all("p", class_="lead"))

    # Get the text from the tags/soup
    p_tag = soup.find('p')
    if p_tag:
       print(p_tag.get_text())
    else:
        print("No <p> tag found in the HTML content.")

    # Get all the anchor tags from the page
    all_links = set()

    # Get all the links on the page:
    for link in anchors:
        if(link.get('href') != '#'): 
            linkText = link.get('href')
            all_links.add(link)
            print(linkText)
    # Return the scraped content
    # Redirect the output to a file
    with open('out1.txt', 'a',encoding='utf-8') as f:
        sys.stdout = f
        print(f"URL: {url}")
        print("Title:", title.get_text())
        print("\nParagraphs:")
        for para in paras:
            print(para.get_text())
        print("\nLinks:")
        for link in all_links:
            print(link.get('href'))
        print("="*50)
def distribute_scraping():
    # Take input URLs from user
    urls = []
    num_urls = int(input("Enter the number of URLs to scrape: "))
    for i in range(num_urls):
        url = input(f"Enter URL {i+1}: ")
        urls.append(url)
        
    with multiprocessing.Pool() as pool:
        results = pool.map(scrape_website, urls)
        # Calculate percentage of cores used
        num_cores = multiprocessing.cpu_count()
        num_active_procs = len(multiprocessing.active_children())
        percent_cores_used = (num_active_procs / num_cores) * 100
        print(f"{percent_cores_used}% of cores used.")


if __name__ == '__main__':
    #give the input url:
    distribute_scraping()


print(f"Number of CPU cores used: {multiprocessing.cpu_count()}")
   