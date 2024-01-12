# Jinja : Jinja2 is one of the most used template engines for Python.
#
# Jinja install : pip install Jinja2
# 설치 위치 : C:\Python34\Lib\site-packages\jinja2-2.8-py3.4.egg

from jinja2 import Template

t = Template('Hello {{name}}')
r = t.render(name='Python')
print(r)

import json
import csv
import webbrowser

def wifi():
    wifi = []

    with open('wifi.csv', encoding='utf-8') as f:
        f.readline()
        f.readline()

        reader = csv.reader(f)
        for line in reader:
            # [{'x':127, 'y':37}, {'x':127, 'y':37} .. ]
            coord = {}
            coord['x'] = line[3]
            coord['y'] = line[4]

            wifi.append(coord)

    with open('map.html') as f:
        with open('output.html', 'w') as w:
            # javascript에서 실행될 수 있도록 json str 형식으로 변환
            json_location = json.dumps(wifi)

            t = Template(f.read())
            r = t.render({'data': json_location})
            w.write(r)

    webbrowser.open('output.html')

wifi()



