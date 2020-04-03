import xadmin
from django.http import HttpResponse
from xadmin import views

from apps.blog.models import Blog, Article, Fans
from xadmin.plugins.actions import BaseActionView

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True  # 支持切换主题

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "后台管理系统"  # 设置站点标题
    site_footer = "后台管理系统"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

## 整体站点设计
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)


class BlogAction(BaseActionView):
    '''
        1.继承特定类对象
        2.blog模块动作:可以批量处理选中的querryset对象
    '''
    action_name = "批量更新"    #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
    description = "批量更新"

    model_perm = 'change'  #: 该 Action 所需权限
    # 而后实现 do_action 方法
    def do_action(self, queryset):
        # queryset 是包含了已经选择的数据的 queryset
        for obj in queryset:
            print(obj.id)
        # 返回 HttpResponse
        return HttpResponse("成功操作对应内容")



class BlogAdmin(object):
    '''
        模型类配置
    '''
    actions = [BlogAction, ]   #自定义的函数方法注册
    # 列表页相关操作
    # list_display = ['id', 'name', 'price', 'create_time', 'category']     #列表页展示哪些字段
    list_editable = ['price', 'name']    #在列表页上可以直接进行编辑操作
    show_detail_fields = ['name']   #列表页快速显示详情
    list_export = ['xls', 'csv', 'xml']  # 在列表页进行文件的导出操作
    list_export_fields = ('price', 'name')  # 导出文件的字段
    refresh_times = [3, 5]  # 可选以支持按多长时间(秒)刷新页面
    readonly_fields = ['create_time']  #只读字段限制
    list_per_page = 20  #每页显示的数量
    aggregate_fields = {"price": "max"} #  列聚合，可用的值："count","min","max","avg",  "sum"
    # ########################  过滤相关操作 ########################
    search_fields = ['name']        #可以根据哪些字段进行过滤:内部使用的是模糊匹配
    list_filter = ['category',"price"]      #分类目录,聚合操作选出种类的个数,然后进行filter删选
    ordering = ["create_time"] #默认排序字段
    ############### 修改删除相关操作 ######################
    reversion_enable = True         #还原按钮,删除的信息可以还原
    ############### 添加数据相关操作 ############
    # 添加数据时候，一步一步提供数据操作指导内容
    wizard_form_list = [
        ("基础信息", ("name", "price",)),
        ("其它信息", ("category", "comment")),
    ]



    def show_tags(self, obj):
        tag_list = []
        for tag in obj.tags.all():
            tag_list.append(tag.name)
        return ','.join(tag_list)

    show_tags.short_description = '标签'

    ####################### 图表信息 ############################
    data_charts = {
        "user": {'title': u"统计", "x-field": "create_time", "y-field": ("price", ), "order": ('create_time',)},
    }

xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Article)
xadmin.site.register(Fans)

