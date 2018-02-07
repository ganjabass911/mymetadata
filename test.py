import dbd2xml as r2m
import xml2dbd as x2r


ram = x2r.start_convert("tasks.xml")
file_xml = r2m.start_convert(ram)

print(file_xml.toprettyxml(encoding='utf-8').decode('utf-8'))
