### Twitter search and sentiment analysis using streamlit

Simple search using streamlit and python requests with fake IE user agent to scrap tweets from the old version of twitter.

Using NLTK Vader for sentiment analysis and ploting the results for each search.

It might seem to be slow, but this mini-app is scrapping all the pages in the search and saving the data into a csv file, so next time when you search for something it will load instantly.


### Why requests and not Selenium ?

Well, obviously using python requests is faster and nicer than using Selenium.

However it depends on the case, as if the websit is using client-side rendering then Selenium would be the best choice.


### Run

```bash
pip install streamlit

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py

```



### Screenshot

![Alt text](https://raw.github.com/cristianexer/Quick-twitter-sentiment-analysis/master/screenshot.png "Screenshot")