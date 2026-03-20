import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import time

def crawl_clothing_sites(dimensions, description):
    """
    Crawl multiple clothing websites for matches
    """
    results = []
    
    sites = [
        crawl_target(dimensions, description),
        crawl_ebay(dimensions, description),
        crawl_walmart(dimensions, description)
    ]
    
    for site_results in sites:
        results.extend(site_results)
    
    return results

def crawl_target(dimensions, description):
    """Crawl Target for clothing matches"""
    try:
        size = dimensions.get('size', '').strip()
        query = f"{description.strip()} {size}"
        
        url = f"https://www.target.com/s?searchTerm={query}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = []
            
            for item in soup.find_all('div', {'class': 'h-padding-b-tight'}):
                title_elem = item.find('a')
                price_elem = item.find('span', {'class': 'h-text-red'})
                
                if title_elem:
                    results.append({
                        'title': title_elem.text.strip()[:80],
                        'price': price_elem.text.strip() if price_elem else 'N/A',
                        'url': 'https://target.com' + title_elem.get('href', ''),
                        'source': 'Target'
                    })
            
            return results[:5]
        else:
            print(f"Target returned status {response.status_code}")
            return []
    except Exception as e:
        print(f"Target crawler error: {e}")
        return []

def crawl_ebay(dimensions, description):
    """Crawl eBay for clothing matches"""
    try:
        size = dimensions.get('size', '').strip()
        query = f"{description.strip()} {size}"
        
        url = f"https://www.ebay.com/sch/i.html?_nkw={query}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = []
            
            for item in soup.find_all('div', {'class': 's-item'}):
                title = item.find('h2')
                price = item.find('span', {'class': 's-item__price'})
                link = item.find('a', {'class': 's-item__link'})
                
                if title and link:
                    results.append({
                        'title': title.text.strip()[:80],
                        'price': price.text.strip() if price else 'N/A',
                        'url': link.get('href', ''),
                        'source': 'eBay'
                    })
            
            return results[:5]
        else:
            print(f"eBay returned status {response.status_code}")
            return []
    except Exception as e:
        print(f"eBay crawler error: {e}")
        return []

def crawl_walmart(dimensions, description):
    """Crawl Walmart for clothing matches"""
    try:
        size = dimensions.get('size', '').strip()
        query = f"{description.strip()} {size}"
        
        url = f"https://www.walmart.com/search?q={query}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = []
            
            for item in soup.find_all('div', {'class': 'mb0 ph1 ph2-xl pb3-xl'}):
                title = item.find('span', {'class': 'lh-title'})
                price = item.find('div', {'class': 'lh-copy black'})
                link = item.find('a')
                
                if title and link:
                    results.append({
                        'title': title.text.strip()[:80],
                        'price': price.text.strip() if price else 'N/A',
                        'url': 'https://walmart.com' + link.get('href', ''),
                        'source': 'Walmart'
                    })
            
            return results[:5]
        else:
            print(f"Walmart returned status {response.status_code}")
            return []
    except Exception as e:
        print(f"Walmart crawler error: {e}")
        return []