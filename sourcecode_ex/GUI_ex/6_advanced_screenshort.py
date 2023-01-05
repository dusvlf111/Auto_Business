import keyboard, time
from PIL import ImageGrab

def screenshot():
    #년월일분 밑줄로 표시
    curr_time = time.strftime("_%Y_%m_%d_%H_%S")
    img = ImageGrab.grab()
    img.save('image{}.png'.format(curr_time))
    
keyboard.add_hotkey('F9', screenshot)
#키보드 핫키 등록 사용자가 F9키를 누르면 스크린 샷 저장
#keyboard.add_hotkey('ctrl+shift+s', screenshot)
#           컨트롤 쉬프트 s 스크린샷됨
keyboard.wait('esc') #사용자가 esc를 누를 땎지 프로그램 수행
