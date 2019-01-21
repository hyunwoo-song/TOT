import os

os.chdir(r'C:\Users\student\hw\day02\dummy')
# print(os.getcwd())
for filename in os.listdir('.'): # .은 현재 폴더 
    # 1. replace 함수이용, 새로운 파일이름 생성
    new_filename = filename.replace('합격자_0_지원자', '합격자_')
    # 2. os.rename 함수 이용, 파일이름 변경
    os.rename(filename, new_filename) 
   
# 합격자_0_ 누구누구.txt        