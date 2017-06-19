val = input('문자 코드값을 입력하세요:')
val = int(val)

try:
    ch=chr(val)
    # chr() 는 ord() 의 반대기능을 한다.
    # chr 로 정수값을 입력하면 정수값에 해당하는 문자를 리턴한다.
    print('코드값: %d[%s], 문자:%s' %(val, hex(val),ch))
except ValueError:
    print('입력한 <%d>에 대한 문자가 존재하지 않습니다!' %val)