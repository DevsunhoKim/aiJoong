# 필요한 라이브러리를 불러옵니다.
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# 데이터를 불러옵니다.
data = pd.read_csv('shipping_data.csv')

# 데이터를 전처리합니다.
stop_words = set(stopwords.words('english'))
vectorizer = TfidfVectorizer(stop_words=stop_words)
X = vectorizer.fit_transform(data['text'])
y = data['label']

# 학습 데이터와 테스트 데이터를 나눕니다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델을 학습합니다.
clf = MultinomialNB()
clf.fit(X_train, y_train)

# 모델을 평가합니다.
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# 1. pandas를 사용하여 shipping_data.csv 파일에서 데이터를 로드합니다.
# nltk를 사용하여 영어 불용어를 제거하고 TfidfVectorizer를 사용하여 문서에서 중요한 단어를 추출하여 입력 데이터를 전처리합니다.
# scikit-learn을 사용하여 입력 데이터를 학습 및 테스트 세트로 분할합니다.
# scikit-learn을 사용하여 나이브 베이즈 분류기를 학습하고, 테스트 세트에서 성능을 측정합니다.
# 이 코드는 여러 알고리즘과 기술을 사용할 수 있습니다. 따라서 데이터와 문제의 세부 정보에 따라 코드를 조정해야 할 수 있습니다.