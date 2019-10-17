import xadmin

from .models import Photos,PhotoDetail


xadmin.site.register(Photos)
xadmin.site.register(PhotoDetail)