import re

str_test = '''
<script src="https://static-jw.msstatic.com/huya-sentry/bundle.min.js" crossorigin="anonymous"></script>
<script nonce="">
'''
pattern = re.compile(r'<script src="(https://[\w\-/\.]*?\.js)')
search_result = re.findall(pattern,str_test)
print(search_result)