import pymysql as pymysql

from Common.CommonHelpers.credentialsHelper import CredentialsHelper


class DBHelpers(object):
    def __init__(self):
        cred_helpers = CredentialsHelper()
        cred = cred_helpers.get_db_credentials()
        self.host = 'localhost'
        self.db_user = cred['db_user']
        self.db_password = cred['db_password']
        self.connection = pymysql.connect(self.host, self.db_user, self.db_password)

    def execute_select(self, sql):
        try:
            cur = self.connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception("Failed running sql {}. Error: {}".format(sql, str(e)))
        finally:
            self.connection.close()
