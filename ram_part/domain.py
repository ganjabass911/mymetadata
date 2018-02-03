class Domain:
    def __init__(self):
        self.id = None
        self.name = None
        self.description = None
        self.data_type_id = None
        self.length = None
        self.char_length = None
        self.precision = None
        self.scale = None
        self.width = None
        self.align = None
        self.show_null = None
        self.show_lead_nulls = None
        self.thousands_separator = None
        self.summable = None
        self.case_sensitive = None
        self.uuid = None

#
# s = """\
#     id integer primary key autoincrement default(null),
#     table_id integer not null,                          -- идентификатор таблицы (dbd$tables)
#     name varchar default(null),                         -- имя индекса
#     local boolean default(0),                           -- показывает тип индекса: локальный или глобальный
#     kind char default(null),                            -- вид индекса (простой/уникальный/полнотекстовый)
#     uuid varchar unique not null COLLATE NOCASE   """""
# lines = s.split('\n')
# words = []
# for line in lines:
#     words.append(line.split(" ")[4])
#     # print(line.split(" "))
# # print(words)
#
# s = """ = None
#     self.""".join(words)
# print("    self." + s + " = None")