import xadmin
from .models import CodingSubmission,SourceCode

xadmin.site.register(CodingSubmission)
xadmin.site.register(SourceCode)

