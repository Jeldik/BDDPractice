from Common.CommonHelpers.dbHelpers import DBHelpers


class UsersDAO(object):
    def __init__(self):
        self.db_helper = DBHelpers()

    def get_user_by_email(self, email):
        sql = "SELECT * FROM local.wp_posts WHERE email = '{}';".format(email)
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql
