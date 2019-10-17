from rest_framework.pagination import PageNumberPagination
from django.core.files.storage import FileSystemStorage
from django.conf import settings
class MyPagination(PageNumberPagination):
    """
    自定义的分页功能
    """
    #默认每页显示的个数
    page_size = 6
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'

    #最多能显示多少页
    #max_page_size = None


class FileTooLarge(Exception):
    """
    限制上传文件大小异常，可单独创建exception.py文件保存该类
    """

class LiterDocStorage(FileSystemStorage):
	# location和base_url均可自定义，定义后settings中的设置就会失效，不建议在这里修改
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # 初始化，location
        super(LiterDocStorage, self).__init__(location, base_url)

    def _save(self, name, content):
        """重写限制文件大小为15MB"""
        if content.size > settings.MAX_FILE_SIZE:
            raise FileTooLarge('文件应小于%sMB' % int((settings.MAX_FILE_SIZE / (1024 * 1024))))
        return super(LiterDocStorage, self)._save(name, content)



