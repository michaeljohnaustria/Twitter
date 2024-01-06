from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Meep

# Unregister Groups
admin.site.unregister(Group)

# Define ProfileInline before using it in UserAdmin
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Display username field and Profile inline on admin page
    fields = ["username"]
    inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Register User and Profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

# Register Meeps
admin.site.register(Meep)