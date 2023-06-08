import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import matplotlib.font_manager as fm


excel_file = pd.read_excel('data1.xlsx', usecols='A')


file_names = excel_file.iloc[:, 0].tolist()


tally = {}
for name in file_names:
    if name in tally:
        tally[name] += 1
    else:
        tally[name] = 1


output_df = pd.DataFrame({'Item': list(tally.keys()), 'Quantity': list(tally.values())})


output_df = output_df.sort_values(by='Quantity', ascending=False)


today = date.today().strftime("%Y%m%d")


output_file = f"tally_results_{today}.xlsx"


output_df.to_excel(output_file, index=False)


plt.bar(output_df['Item'], output_df['Quantity'])
plt.xlabel('Item')
plt.ylabel('Quantity')
plt.title('Tally Results')
plt.xticks(rotation=90)
plt.show()

print(f"Tally results have been written to {output_file}.")


font_path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=12)


plt.bar(output_df['Item'], output_df['Quantity'])
plt.xlabel('품목', fontproperties=fontprop)  
plt.ylabel('수량', fontproperties=fontprop)  
plt.title('품목별 수량 결과', fontproperties=fontprop)  
plt.xticks(rotation=90, fontproperties=fontprop)  
plt.show()



