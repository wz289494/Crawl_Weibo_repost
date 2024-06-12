import pymysql

class Store(object):
    def store_post_mode_mysql(self, db_name, tb_name, data_list):
        """
        Store post data into a MySQL database.

        Parameters:
        db_name (str): The name of the database.
        tb_name (str): The name of the table.
        data_list (list): A list of dictionaries containing post data.

        Returns:
        None
        """
        try:
            # Connect to the database
            self.db = pymysql.connect(host='localhost', user='root', passwd='wz131', port=3306)
            self.cursor = self.db.cursor()
            # print('-Connection successful-')

            # Check and create database if it does not exist
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            # print('-Database checked-')

            # Select the database
            self.cursor.execute(f"USE {db_name}")

            # Create the table
            self.__create_user_table(tb_name)

            # Insert data
            self.__user_insert(tb_name, data_list)
            # print('-Inserting data-')

            # Close the connection
            self.db.close()
            # print('-Connection closed-')

        except pymysql.MySQLError as e:
            print(f"Error connecting to the database: {e}")

    def __create_user_table(self, tb_name):
        """
        Create a table for storing post data if it does not exist.

        Parameters:
        tb_name (str): The name of the table.

        Returns:
        None
        """
        try:
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {tb_name} (
                MAIN_ID INT AUTO_INCREMENT PRIMARY KEY,
                微博ID TEXT,
                微博文本内容 TEXT,
                创建时间 TEXT,
                用户ID TEXT,
                用户昵称 TEXT,
                是否认证用户 TEXT,
                点赞数 TEXT,
                转发数 TEXT,
                评论数 TEXT
            );
            """
            self.cursor.execute(create_table_query)
            # print('-Table checked-')

        except pymysql.MySQLError as e:
            print(f"Error creating table: {e}")

    def __user_insert(self, tb_name, data_list):
        """
        Insert post data into the table.

        Parameters:
        tb_name (str): The name of the table.
        data_list (list): A list of dictionaries containing post data.

        Returns:
        None
        """
        try:
            insert_query = f"""
            INSERT INTO {tb_name} (微博ID, 微博文本内容, 创建时间, 用户ID, 用户昵称, 是否认证用户, 点赞数, 转发数, 评论数)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Execute multiple insertions, each element is a dictionary
            for post in data_list:
                self.cursor.execute(insert_query, (
                    post['微博ID'], post['微博文本内容'], post['创建时间'],
                    post['用户ID'], post['用户昵称'], post['是否认证用户'], post['点赞数'], post['转发数'], post['评论数']
                ))

            self.db.commit()
            print('-Data inserted successfully-')

        except pymysql.MySQLError as e:
            print(f"Error during insertion: {e}")
            self.db.rollback()
