# Create Instance Using AWS RDS

1. Login AWS Console
2. Search for RDS --> open RDS Dashboard
3. create database --> standard create --> Engine MYSQL --> Edition- mySQL Comm
4. Version --> 8.0.43 --> Template Go with Free tier
5. Settings --> Type Name of Database --> pw
6. credentials set username admin, set your own password don't include @
7. others keep with the default settings and create Database.
8. IN RDS database make sure the security group has the port open 3306

# Create Ubuntu instanse with default sg 22 port open

1. connect with the instance with SSH
2. install mysql-client
    sudo apt update && sudo apt install mysql-client -y
3. let's connect with RDS DB:
    mysql -h <enter_end_point_db> -u admin -p
4. enter your generated password
5. you will be connected with RDS from instance
6. you can execute some queries

    show databases;
    create database pw;
    select NOW();

7. check outputs.