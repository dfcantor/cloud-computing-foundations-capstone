{"filter":false,"title":"test_conn.py","tooltip":"/eb-flask/test_conn.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["import psycopg2","","# Set the connection parameters","host = \"database-1.c1istjcucv5g.us-east-1.rds.amazonaws.com\"","port = 5432","dbname = \"shapeseekr\"","user = \"postgres\"","password = \"postgres\"","","try:","    # Try to connect to the database","    conn = psycopg2.connect(","        host=host, port=port, dbname=dbname, user=user, password=password","    )","","    # If the connection is successful, print a success message","    print(\"Connection successful!\")","","    # Close the connection","    conn.close()","","except psycopg2.Error as e:","    # If the connection fails, print the error message","    print(\"Unable to connect!\")","    print(e)",""],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":4},"end":{"row":9,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1681968394613,"hash":"fbe049d0f207e801b50cbaabc18cb28d2984b320"}