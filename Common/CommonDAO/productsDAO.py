from Common.CommonHelpers.dbHelpers import DBHelpers

class ProductsDAO(object):
    def __init__(self):
        self.db_helper= DBHelpers()

    def get_products_from_db(self):
        sql = "SELECT * FROM local.wp_posts WHERE post_type = 'product';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql