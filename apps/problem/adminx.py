import xadmin
from .models import CodingProlemInfo, OtherProblem, ProblemTages


class CodingProlemInfoAdmin(object):
    style_fields = {"pro_desc": "ueditor", "pro_input": "ueditor",
                    "pro_output": "ueditor", "sample_input": "ueditor",
                    "sample_output": "ueditor"}


xadmin.site.register(ProblemTages)
xadmin.site.register(CodingProlemInfo, CodingProlemInfoAdmin)
xadmin.site.register(OtherProblem)

