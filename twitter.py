import pandas as pd
import requests as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from os.path import exists
import urllib.parse

twitter_selectors = {
    'post': '.tweet',
#    'full_name': '.fullname',
    'username': '.username',
    'content': '.tweet-text'
    
}

def get_html(url,headers={'User-Agent': UserAgent().ie }):
    return req.get(url=url, headers=headers).text
    
def get_soup(html):
    return BeautifulSoup(html,'html.parser')
    
def get_next_cursor(soup):
    return soup.select_one()
    
def get_tweets(soup):
    tweets = list()
    selected_tweets = soup.select(twitter_selectors['post'])
    for tweet in selected_tweets:
#        full_name = tweet.select_one(twitter_selectors['full_name']).text
        username = tweet.select_one(twitter_selectors['username']).text
        content = tweet.select_one(twitter_selectors['content']).text
        tweets.append({
#                'full_name': full_name,
                'username': username,
                'content': content,
        })
        
    return tweets
    
    
def get_tweets_from(path):
    return pd.read_csv(path)
    
    
def get_tweets_df(keyword):
    file_keyword = keyword.replace(" ","_")
    tweets_file = f'{file_keyword}.csv'
    url = f'https://mobile.twitter.com/search?q={urllib.parse.quote_plus(keyword)}'
    if not exists(tweets_file):
        tweets = []
        stop = True
        while(stop != False):
            html_data = get_html(url=url)
            soup = get_soup(html=html_data)
            tweets+=get_tweets(soup=soup)
            next = soup.select_one('.w-button-more a')
            if next:
                url = 'https://mobile.twitter.com' + next['href']
                print(f'Next cursor: {next["href"]}')
            else:
                stop = False
            

        df = pd.DataFrame.from_dict(tweets)
        
        df.to_csv(tweets_file,index=False)
    else:
        df = get_tweets_from(tweets_file)
        
    return df
