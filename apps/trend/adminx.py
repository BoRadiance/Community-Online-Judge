import xadmin
from .models import TrendClass,TrendComment,Trend,TrendUpDown,TrendPhoto




xadmin.site.register(TrendClass)
xadmin.site.register(Trend)
xadmin.site.register(TrendPhoto)
xadmin.site.register(TrendUpDown)
xadmin.site.register(TrendComment)
