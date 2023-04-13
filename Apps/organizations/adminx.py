import xadmin

from Apps.organizations.models import Instructors, Organizations


class InstructorAdmin(object):
    list_display = ['org', 'name', 'work_position']
    search_fields = ['org', 'name', 'work_position']
    list_filter = ['org', 'name', 'work_position']


class OrganizationsAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'number_of_beFav']
    search_fields = ['name', 'desc', 'click_nums', 'number_of_beFav']
    list_filter = ['name', 'desc', 'click_nums', 'number_of_beFav']


xadmin.site.register(Organizations, OrganizationsAdmin)
xadmin.site.register(Instructors, InstructorAdmin)
