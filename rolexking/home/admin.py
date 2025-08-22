from django.contrib import admin
from .models import Rolex_Number
from django.db import models
from django.utils import timezone
import pytz
# Register your models here.

class Rolex_NumberAdmin(admin.ModelAdmin):
    list_display = ('User', 'Today_Number', 'Sign', 'Description', 'Created_at', 'Week', 'Month', 'Year')
    search_fields = ('Sign', 'Created_at')
    list_filter = ('Sign', 'Created_at', 'User')
    list_per_page = 10

    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 2, 'cols': 30})},
    }

    def get_readonly_fields(self, request, obj=None):
        if obj:
            india_tz = pytz.timezone('Asia/Kolkata')
            now = timezone.now().astimezone(india_tz)
            if (now - obj.Created_at).total_seconds() > 86400:  # 24 hours in seconds
                # Make all fields readonly except 'id'
                return [field.name for field in self.model._meta.fields if field.name != 'id']
        return super().get_readonly_fields(request, obj)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Limit User dropdown to only the logged-in user and set as default
        form.base_fields['User'].queryset = form.base_fields['User'].queryset.filter(id=request.user.id)
        form.base_fields['User'].initial = request.user
        return form

admin.site.register(Rolex_Number, Rolex_NumberAdmin)