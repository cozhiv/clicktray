"""Constants that will be reused"""

db_name = "mousetray.db"
table_name = "picpool"
create_table = "CREATE TABLE IF NOT EXISTS {} (x TEXT, y TEXT, pic BLOB)".format(table_name)
read_data = "SELECT x, y, pic FROM picpool"
