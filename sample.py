# 필요한 라이브러리를 불러옵니다.
import pandas as pd
import nltk
nltk.download('stopwords')
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

"""Python 코드를 실행 파일로 배포하려면 PyInstaller라는 도구를 사용할 수 있습니다. PyInstaller는 Python 코드를 Windows, macOS 및 Linux용 독립 실행형 실행 파일로 패키징할 수 있는 크로스 플랫폼 도구입니다.


다음은 PyInstaller를 사용하여 Windows용 실행 파일을 만드는 단계입니다.


PyInstaller 설치: pip를 사용하여 PyInstaller를 설치할 수 있습니다. 터미널 또는 명령 프롬프트를 열고 다음 명령을 실행합니다.


Copy code
pip install pyinstaller
스크립트 만들기: 실행 파일로 패키징하려는 Python 스크립트를 만듭니다. 스크립트가 오류 없이 실행되고 필요한 모든 종속성이 포함되어 있는지 확인하십시오.
스크립트 패키징: 터미널 또는 명령 프롬프트를 열고 Python 스크립트가 포함된 디렉터리로 이동합니다. 다음 명령을 실행하여 스크립트를 패키징합니다.


css
Copy code
pyinstaller --onefile your_script_name.py
이렇게 하면 dist 디렉토리에 단일 실행 파일이 생성됩니다.


실행 파일 테스트: dist 디렉토리로 이동하여 실행 파일을 실행합니다. 스크립트가 예상대로 실행되고 필요한 모든 종속성이 포함되어 있는지 확인하십시오.
실행 파일 배포: 실행 파일을 다른 Windows 사용자에게 배포할 수 있습니다. Python 또는 종속성을 설치하지 않고 실행 파일을 실행할 수 있습니다.
PyInstaller는 모든 Python 스크립트를 독립 실행형 실행 파일로 패키징하지 못할 수 있습니다. 경우에 따라 실행 파일로 올바르게 작동하도록 스크립트를 수정하거나 추가 종속성을 포함해야 할 수 있습니다.


요약하면 PyInstaller는 Python 코드를 Windows, macOS 및 Linux용 독립형 실행 파일로 배포할 수 있는 강력한 도구입니다. 다음 단계에 따라 Python 스크립트용 실행 파일을 만들고 배포할 수 있습니다."""


"""다음은 Python 실행 파일에 GUI를 추가하기 위해 따를 수 있는 기본 단계입니다.


GUI 툴킷 선택: Python 버전 및 운영 체제와 호환되는 GUI 툴킷을 선택합니다. Tkinter는 대부분의 Python 설치에 포함되어 있지만 PyQt 및 wxPython에는 추가 설치 단계가 필요합니다.
GUI 디자인: GUI 툴킷의 위젯을 사용하여 GUI 레이아웃을 디자인합니다. 필요에 따라 창, 버튼, 레이블 및 기타 GUI 구성 요소를 만듭니다. 대부분의 GUI 툴킷을 사용하면 드래그 앤 드롭 인터페이스를 사용하여 GUI를 시각적으로 디자인할 수 있습니다.
기능 추가: Python 코드를 추가하여 GUI 구성 요소와의 사용자 상호 작용을 처리합니다. 예를 들어 버튼을 클릭할 때 특정 작업을 수행하도록 버튼에 이벤트 핸들러를 추가할 수 있습니다.
실행 파일 빌드: PyInstaller 또는 다른 도구를 사용하여 Python 코드와 GUI를 독립형 실행 파일로 패키징합니다.
실행 파일 테스트: 실행 파일을 테스트하여 GUI가 예상대로 작동하는지 확인합니다.
실행 파일 배포: Python 또는 종속성을 설치하지 않고 실행할 수 있는 사용자에게 실행 파일을 배포합니다.

Python 실행 파일에 GUI를 추가하려면 패키지에 포함할 추가 종속성 및 라이브러리가 필요할 수 있습니다. GUI 구성 요소와 올바르게 상호 작용하려면 Python 코드를 수정해야 할 수도 있습니다.


요약하면 Python 실행 파일에 GUI를 추가하려면 GUI 툴킷 선택, GUI 설계, 기능 추가, 실행 파일 빌드, 실행 파일 테스트 및 사용자 배포가 필요합니다. 다음 단계에 따라 Python 코드에 대한 사용자 친화적인 인터페이스를 생성하고 독립 실행형 실행 파일로 배포할 수 있습니다."""