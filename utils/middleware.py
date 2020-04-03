def simple_middleware(get_response):
    # 此处编写的代码仅仅在Django第一次配置和初始化的时候执行一次
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用
        print("请求前处理")
        response = get_response(request)
        print("请求后处理")
        # 此处编写的代码会在每个请求处理视图之后被调用
        return response
    return middleware




