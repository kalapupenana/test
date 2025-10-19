from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
try:
    from import_export.admin import ImportExportModelAdmin
    BaseAdmin = ImportExportModelAdmin
except Exception:
    BaseAdmin = admin.ModelAdmin

from .models import Branch, Member, User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Church Roles", {"fields": ("branch", "is_minister")}),)
    list_display = ("username", "first_name", "last_name", "branch", "is_minister", "is_staff", "is_superuser")
    list_filter = ("branch", "is_minister", "is_staff", "is_superuser", "is_active")

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)

class MemberAdminBase(BaseAdmin):
    list_display = ("first_name", "last_name", "branch", "tf_code", "status", "dob")
    list_filter = ("branch", "status", "tf_code")
    search_fields = ("first_name", "last_name")
    autocomplete_fields = ("branch",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Superusers or staff (not marked as minister) see everything
        if request.user.is_superuser or (request.user.is_staff and not request.user.is_minister):
            return qs
        # Ministers see only their branch
        if request.user.is_minister and request.user.branch_id:
            return qs.filter(branch=request.user.branch)
        # Default: nothing
        return qs.none()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "branch" and request.user.is_minister and request.user.branch_id:
            kwargs["queryset"] = Branch.objects.filter(id=request.user.branch_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or (request.user.is_staff and not request.user.is_minister):
            return True
        if request.user.is_minister and obj is not None:
            return obj.branch_id == request.user.branch_id
        return True

    def has_add_permission(self, request):
        if request.user.is_superuser or (request.user.is_staff and not request.user.is_minister):
            return True
        return bool(request.user.is_minister and request.user.branch_id)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or (request.user.is_staff and not request.user.is_minister):
            return True
        if request.user.is_minister and obj is not None:
            return obj.branch_id == request.user.branch_id
        return False

@admin.register(Member)
class MemberAdmin(MemberAdminBase):
    pass
