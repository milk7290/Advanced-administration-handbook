import re,base64,io
from PIL import Image
src='./index.html'
dst='./index.public.html'
s=open(src).read()
# 1x1 투명 PNG (밥테일 로고 제거)
buf=io.BytesIO(); Image.new('RGBA',(1,1),(0,0,0,0)).save(buf,'PNG')
blank='data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode()
s,n=re.subn(r"const DEFAULT_LOGO = 'data:image/png;base64,[A-Za-z0-9+/=]+';","const DEFAULT_LOGO = '"+blank+"';",s)
assert n==1
# 기본 상호명/표시방식/제목
s=s.replace('placeholder="예: 행복한 빵집" value="밥테일베이커리"','placeholder="예: 행복한 빵집" value="우리 가게"')
s=s.replace('<option value="logo">로고 이미지</option>\n            <option value="name">상호명 글자</option>','<option value="logo">로고 이미지</option>\n            <option value="name" selected>상호명 글자</option>')
s=s.replace('<title>밥테일 즉석 인쇄</title>','<title>즉석 사진 인쇄</title>')
open(dst,'w').write(s)
bad=[k for k in ['BOBTAIL','밥테일','Bobtail','bobtail'] if k in s]
print('public build ok; leftover brand strings:',bad,'| size',len(s))
