import os
import json

from contextlib import ExitStack

from aurora_data_api import connect

from dotenv import load_dotenv


load_dotenv()


def get_data_from_db(cur, *, table_name: str, field_name: str):
    query = (
        f'SELECT id, {field_name} FROM {table_name}'
    )
    cur.execute(query)
    return {
        item[1]: item[0]
        for item in cur.fetchall()
    }


list_tables = [
    ('province', 'name'),
    ('district', 'name'),
    ('ward', 'name'),
    ('working_status', 'name'),
    ('employment_contract', 'name'),
    ('teaching_title', 'name'),
    ('academic_title', 'name'),
    ('ethnics', 'name'),
    ('religion', 'name'),
    ('degree', 'name'),
]


with ExitStack() as stack:
    conn = stack.enter_context(
        connect(
            os.getenv('INSTANCE_ARN'),
            os.getenv('SECRET_ARN'),
            database=os.getenv('DB_NAME')
        )
    )
    cursor = stack.enter_context(conn.cursor())
    for table in list_tables:
        tbl_name = table[0]
        field = table[1]
        with open(f'src/output/{tbl_name}.json', 'w+') as f:
            data = get_data_from_db(cursor,
                                    table_name=tbl_name,
                                    field_name=field)
            json.dump(data, f, ensure_ascii=False, indent=4)
