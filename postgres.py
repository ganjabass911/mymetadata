import psycopg2

from metadata import Field, Constraint

base_type = dict(
    INTEGER="int",
    BLOB="bytea",
    BOOLEAN="boolean",
    BYTE="smallint",
    LARGEINT="bigint",
    SMALLINT="smallint",
    WORD="smallint",
    DATE="date",
    TIME="time",
    MEMO="text",
    FLOAT="numeric",
    STRING="varchar",
    CODE="varchar"
)


def change_name(name):
    i = 0
    name.find(' ', i)
    name[i] = '_'


def find_type(sql_type):
    if sql_type in base_type:
        return base_type[sql_type]


def creat_DB(schema):
    # Создаем соединение с нашей базой данных
    connect = psycopg2.connect("dbname ='{dbname}' user='{user}' host='{host}' port='{port}' password='{pwd}'".format(
        dbname="metadata",
        user="postgres",
        host="localhost",
        port="39414",
        pwd="1"
    ))

    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = connect.cursor()
    # Удаляем старую и Создаем новую схему
    cursor.execute("""
        DROP SCHEMA "{}" CASCADE;
        
        
        
        CREATE SCHEMA "{}"
        """.format(schema.name, schema.name, ))

    # Создаем домены
    for domain in schema.domains:
        cursor.execute("""
            CREATE DOMAIN "{}"."{}" AS {}""".format(schema.name, domain.name, find_type(domain.type)))

    # Создаем таблицы
    for table in schema.tables:
        sql = ("""
            CREATE TABLE "{}"."{}" (""".format(schema.name, table.name))
        # Таблицы
        columns = []
        # Primary keys
        pks = []
        # Unique keys
        uks = []
        # Check keys
        cks = []

        # Создаем филды
        for field in table.fields:
            columns.append('"{}" "{}"."{}"'.format(field.name, schema.name, field.domain_id))
        # Создаем кострэйнты
        for constraint in table.constraints:
            if 'PRIMARY' == constraint.constraint_type:
                pks.append(constraint.items)
            elif 'UNIQUE' == constraint.constraint_type:
                uks.append(constraint.items)
            elif 'CHECK' == constraint.constraint_type:
                check = constraint.items.expression.replace('[', '')
                check = check.replace(']', '')
                cks.append('CHECK {}'.format(check))
        if pks:
            columns.append("PRIMARY KEY (\"{}\")".format(', '.join(pks)))
        if uks:
            columns.append('UNIQUE ({})'.format(', '.join(uks)))
        if cks:
            columns += cks
        sql += (', '.join(columns))
        sql += ');'
        cursor.execute(sql)

    # Создаем связи таблиц
    for table in schema.tables:
        for constraint in filter(lambda x: x.kind == "FOREIGN", table.constraints):
            sql1 = 'ALTER TABLE "{}"."{}" ADD {} FOREIGN KEY ("{}") REFERENCES "{}"."{}" '. \
                format(schema.name, table.name, "CONSTRAINT " + constraint.name if constraint.name is not None else "",
                       constraint.items, schema.name, constraint.reference)
            if constraint.id is True:
                sql1 += 'ON DELETE CASCADE;'
            if constraint.id is False:
                sql1 += 'ON DELETE RESTRICT;'
            if constraint.id is None:
                sql1 += 'ON DELETE SET NULL;'
            cursor.execute(sql1)

    # Оздаем идуксы
    for table in schema.tables:
        for index in table.indices:
            cursor.execute('CREATE INDEX {} ON "{}"."{}" ("{}");'.format(index.name if index.name is not None else "",
                                                                         schema.name, table.name, index.fields))
    # Если мы вносим изменения в базу данных - необходимо сохранить транзакцию
    connect.commit()

    # Не забываем закрыть соединение с базой данных
    connect.close()
