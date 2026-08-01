from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    SubscriptionPlan,
    Organization,
    User,
    Team,
    TeamMembership,
    Project,
    UsageTracking,
    Task,
)


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "max_users", "max_projects", "max_teams", "created_at")
    ordering = ("price",)

    # Only platform superusers may see/manage pricing —
    # intentionally separate from the app's OWNER/ADMIN org-level roles.
    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "role", "organization", "is_staff", "is_superuser", "is_active")
    list_filter = ("role", "is_staff", "is_superuser", "is_active", "organization")
    search_fields = ("username", "email", "first_name", "last_name")

    fieldsets = BaseUserAdmin.fieldsets + (
        ("WorkNest", {"fields": ("role", "organization")}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("WorkNest", {"fields": ("role", "organization")}),
    )


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name", "subscription_plan", "is_active",
        "is_subscription_active", "subscription_expires_at",
        "created_by", "created_at",
    )
    list_filter = ("is_active", "subscription_plan")
    search_fields = ("name",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "created_by", "is_active", "created_at")
    list_filter = ("organization", "is_active")
    search_fields = ("name",)


@admin.register(TeamMembership)
class TeamMembershipAdmin(admin.ModelAdmin):
    list_display = ("member", "team", "added_by", "added_at")
    list_filter = ("team",)
    search_fields = ("member__username", "team__name")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name", "organization", "team", "status",
        "deadline", "is_active", "created_by", "created_at",
    )
    list_filter = ("status", "organization", "is_active")
    search_fields = ("name",)


@admin.register(UsageTracking)
class UsageTrackingAdmin(admin.ModelAdmin):
    list_display = ("organization", "active_users", "total_projects", "total_teams", "last_updated")
    search_fields = ("organization__name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "assigned_to", "status", "deadline", "created_by", "created_at")
    list_filter = ("status", "project")
    search_fields = ("title",)