lunch = {
    '벌교꼬막비빔밥':'054-451-5484' ,
    '돌막창':'054-428-1152' ,
    '대패삼겹살':'054-887-4848'
}

import csv


with open('lunch.csv','w',encoding='utf8',newline='') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items(): # 리스트 [(key, value), ...]
        csv_writer.writerow(item)
        
        # f.write(f'{item[0]},{item[1]}\n')
