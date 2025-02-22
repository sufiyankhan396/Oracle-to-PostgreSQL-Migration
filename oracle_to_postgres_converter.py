import re

def convert_sql(oracle_sql):
    oracle_sql = re.sub(r'NUMBER\((\d+),(\d+)\)', r'DECIMAL(\1,\2)', oracle_sql)
    oracle_sql = oracle_sql.replace("VARCHAR2", "VARCHAR")
    oracle_sql = oracle_sql.replace("NUMBER", "SERIAL")  # Assuming primary keys
    return oracle_sql

oracle_schema = open("schema_migration/oracle_schema.sql").read()
postgresql_schema = convert_sql(oracle_schema)

with open("schema_migration/postgresql_schema.sql", "w") as f:
    f.write(postgresql_schema)

print("Schema conversion complete!")
