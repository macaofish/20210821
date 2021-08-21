# 20210821

## Connect to mysql:
1. django version < 2.0, pip install pymysql
   "__init__.py"(under project folder), add "import pymysql" and "pymysql.install_as_MySQLdb()"
   
2. django version >= 2.0, pip install mysqlclient
