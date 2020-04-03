from rest_framework.pagination import PageNumberPagination

class StandardPageNumberPagination(PageNumberPagination):
    '''
        基本分页器的指定,可以继承来拓展对应视图的分页器
    '''
    page_query_param = 'page'  # 前端传递过来的页码信息
    page_size_query_param = 'page_size'  # 前端发送每页数量的关键字参数名称
    max_page_size = 20  # 每页最大数量限制


