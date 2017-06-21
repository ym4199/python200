import os

newfolder = input('생성할 디렉터리 이름을 입력하세요:')
try:
    os.mkdir(newfolder)
    print('[%s]디렉터리를 생성했습니다.' %newfolder)
except Exception as e:
    print(e)