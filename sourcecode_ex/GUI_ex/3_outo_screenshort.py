from PIL import (
    ImageGrab
)

import time, random, os, datetime
ran_num = str(random.randint(1, 1000000))



time.sleep(5)   # 5초 대기 : 사용자가 준비하는 시간
d = datetime.datetime.now()
d_time = str(d.year) + str(d.month) + str(d.day) + '_' + str(d.second)
path_save = 'C:\\Users\\a\\Desktop\\GUI_project\\project\\img_Save\\'+ d_time #경로

# file_name = path_save + datetime.datetime.today()
# print(file_name)
os.mkdir(path_save)

img_save = path_save+'\\'
print(img_save)

photo_range = 20
photo_timespace = 1

for i in range(1, photo_range+1):  # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab()
    img.save(img_save+'image{}.png'.format(i))
    print(
        '{:.1f}%'.format(i/photo_range*100),
        '----------------------image{}.png'.format(i)
        )
    
    time.sleep(photo_timespace)   # 2초 단위
    