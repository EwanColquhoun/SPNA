from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from .models import Document, SPNAMember

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Documents admin for the superuser(admin)
    """

    search_fields = ['title', 'category', 'date_uploaded']
    list_display = (
        'title',
        'category',
        'date_uploaded',
    )
    ordering = ('-date_uploaded',)
 

# @admin.register(SPNAMember)
# class SPNAMemberAdmin(admin.ModelAdmin):
#     """
#     Member admin for the superuser(admin)
#     """
#     search_fields = ['fullname', 'email', 'nursery', 'town_or_city', 'country']
#     list_display = (
#         'fullname',
#         'username',
#         'email',
#         'nursery',
#         'town_or_city',
#         'date_joined',
#     )
#     ordering = ('date_joined',)
 
class MemberInline(admin.StackedInline):
    model = SPNAMember
    can_delete = False
    verbose_name_plural = 'Member'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (MemberInline, )
    list_display = ('username', 'email', 'date_joined', 'get_nursery', 'get_fullname')
    list_select_related = ('spnamember', )

    def get_nursery(self, instance):
        return instance.spnamember.nursery
    get_nursery.short_description = 'Nursery'

    def get_fullname(self, instance):
        return instance.spnamember.fullname
    get_fullname.short_description = 'Full Name'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
