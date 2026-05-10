import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from textblob import TextBlob
import string

nltk.download('punkt')
nltk.download('stopwords')

st.title("NLP Text Analyzer")

text = st.text_area("Enter your text")

if st.button("Analyze"):

    text = text.lower()

    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    words = [word for word in words if word not in string.punctuation]

    stop_words = set(stopwords.words('english'))

    filtered_words = [word for word in words if word not in stop_words]

    word_freq = Counter(filtered_words)
    common_words = word_freq.most_common(5)

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        result = "Positive 😀"
    elif sentiment < 0:
        result = "Negative 😔"
    else:
        result = "Neutral 😐"

    st.write("Total Sentences:", len(sentences))
    st.write("Total Words:", len(words))

    st.subheader("Most Common Words")

    for word, count in common_words:
        st.write(f"{word} : {count}")

    st.subheader("Sentiment")
    st.success(result)
