import xml2ram.execute as x2r
import ram2xml.execute as r2x


print(r2x.start_convert(x2r.start_convert("../tasks.xml")).toprettyxml(encoding='utf-8').decode('utf-8'))

# print((executeX2R.start_convert("../tasks.xml")))
# s=('self.id = None',
#         'self.table_id = None',
#         'self.name = None',
#         'self.local = None',
#         'self.kind = None',
#         'self.uuid = None',
#         'self.fields = None',)
# for i in s:
#     # print(i.find('.'))
#     t=i[i.find('.')+1:i.find(' ')+1]
#     print(' if teg.'+t +' is not None:')
#     print('    index.setAttribute("'+t +'", teg.'+t+')')