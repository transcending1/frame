import json, time

from apps.article.models import Book,Category, Chapter

value = {
    'node_name': "xxx",
    'node_id': 12,
    'need_pay': bool
}
c = Chapter.objects.get(pk=3)

t1 = time.time()
v = json.loads(c.content)
t2 = time.time()

print(t2-t1,'\n', v)






