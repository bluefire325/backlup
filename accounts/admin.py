from django.contrib import admin

from .models import Post
from .models import Schedule_of_events
from .models import Events
from .models import Contestant
from .models import Judge
from .models import Scores
from .models import Catergory
from .models import Reports
from .models import Results



admin.site.register(Post)
admin.site.register(Schedule_of_events)
admin.site.register(Events)
admin.site.register(Contestant)
admin.site.register(Judge)
admin.site.register(Scores)
admin.site.register(Catergory)
admin.site.register(Reports)
admin.site.register(Results)

# Register your models here.
