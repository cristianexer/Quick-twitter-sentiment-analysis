import streamlit as st
from twitter import get_tweets_df
import matplotlib.pyplot as plt
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

st.title('Twitter')
st.subheader("Search")
keyword = st.text_input("Full search")

print(keyword)
if keyword != ' ':
    st.subheader('Extracted Data')
    df = get_tweets_df(keyword=keyword)
    st.write(df)

def get_sentiment_scores(content):
    sid = SentimentIntensityAnalyzer()
    scores = dict([('pos', 0), ('neu', 0), ('neg', 0), ('compound', 0)])

    for c in content:
        ss = sid.polarity_scores(c)
        for k in sorted(ss):
            scores[k] += ss[k]
            
    return scores

if df.size > 0:
    st.subheader('Mean Sentiment Analysis')
    sent_scores = get_sentiment_scores(list(df['content']))
    fig = plt.figure(figsize=[7, 7])
    fig.patch.set_facecolor('white')
    fig.patch.set_alpha(0.0)
    ax = fig.add_subplot(111)
    rows = len(list(df['content']))
    sent_scores['pos'] /= rows
    sent_scores['neu'] /= rows
    sent_scores['neg'] /= rows
    sent_scores['compound'] /= rows
    ax.pie(sent_scores.values(),explode=(0.1,0,0.1,0.3),labels=sent_scores.keys(),autopct='%1.1f%%', startangle=90)
    st.pyplot()

