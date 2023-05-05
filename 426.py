""" 업무자동화를 목표로 하는 코드입니다.
    엑셀 시트의 A열에 있는 품목 명을 취합하여 수량과 csv파일로 만드는 코드입니다.
    현재 가지고 있는 데이터셋은 작성되는 사람에 따라 다른 표기법을 사용하여 수량 종합에 어려움이 있습니다.
    이를 해결하기 위해 인공지능 기술을 사용하여 학습을 시키고 실행 파일로 변환하여 반영구적인 프로그램을 제작하는 것이 최종 목표입니다.
    처리해야 하는 데이터 세트는 data1.xlsx 파일에 저장되어 있습니다."""
import pandas as pd

# 'data1.xlsx'라는 이름의 엑셀 파일을 DataFrame으로 읽어옵니다.
df = pd.read_excel('data1.xlsx')

freq = {}

# DataFrame의 각 행을 반복하여 행을 개별 아이템으로 분할하고 각 아이템의 빈도를 계산합니다.
for row in df.itertuples():
    # 개별 항목으로 분할
    items = row[1].split()

    # 항목의 빈도 계산
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

# 아이템 빈도를 저장하는 딕셔너리를 DataFrame으로 변환하고 빈도를 기준으로 내림차순으로 정렬합니다.
freq_df = pd.DataFrame(list(freq.items()), columns=['Item', 'Frequency'])
freq_df.sort_values(by=['Frequency'], ascending=False, inplace=True)

# DataFrame을 'item_frequencies.csv'라는 CSV 파일로 내보냅니다.
freq_df.to_csv('item_frequencies.csv', index=False) 

# 파이썬 터미널 실행 오류
# 코드 점검, 개발 환경 점검 이상 확인  
# 라이브러리 점검, 실행파일화 
# 관리자 권한 , 접근권한 , 더블체크  
#  
# 
#   