from textblob import TextBlob
#from newspaper import Article

with open('mytxt.txt','r')as f:
    text=f.read()

"""
url="https://indianexpress.com/article/cities/mumbai/thane-man-kills-12-year-old-sister-mistakes-first-period-blood-stains-physical-relationship-8602221/"
article=Article(url)
article.download()
article.parse()
article.nlp()

text=article.summary
print(text)
"""

blob=TextBlob(text)
sentiment=blob.sentiment.polarity  #-1 to 1

print(sentiment)
