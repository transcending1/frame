from apps.blog.models.sql_models import Blog, Article


def new_add():
    '''
        新增一条内容
    '''
    # 平常的表单添加
    # blog = Blog(name="test").save()
    article = Article.objects.get_or_create(name="你好")    # 数据库中不存在就创建

    # 外键添加    情景:一对多,在多表中添加单表实例
    article = Article(name="你好", blog=Blog.objects.get(id=1)).save()  # 情景一:添加记录的时候顺便添加外键


    # 外键添加






if __name__ == "__main__":
    new_add()






