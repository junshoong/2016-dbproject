from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export import resources
from import_export import fields
from import_export.admin import ImportExportMixin

from alumni.models import User


class UserResource(resources.ModelResource):
    id = fields.Field(attribute='id', column_name='연번')
    period = fields.Field(attribute='period', column_name='기수')
    picture = fields.Field(attribute='picture', column_name='사진')
    name = fields.Field(attribute='name', column_name='성명')
    work = fields.Field(attribute='work', column_name='소속')
    work_position = fields.Field(attribute='work_position', column_name='지위')
    login_id = fields.Field(attribute='login_id', column_name='핸드폰')
    work_phone = fields.Field(attribute='work_phone', column_name='직장전화')
    email = fields.Field(attribute='email', column_name='이메일')
    work_address = fields.Field(attribute='work_address', column_name='근무지 주소', readonly=True)

    class Meta:
        model = User
        export_order = (
            'id', 'period', 'picture', 'name', 'work', 'work_position',
            'login_id', 'work_phone', 'email', )
        fields = (
            'id', 'period', 'picture', 'name', 'work', 'work_position',
            'login_id', 'work_phone', 'email', )

        import_id_fields = ('id',)


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('login_id', 'name', 'period', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('login_id', 'password', 'name', 'is_active', 'is_admin',
                  'position', 'position_all', )

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(ImportExportMixin, BaseUserAdmin):
    resource_class = UserResource
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('login_id', 'name', 'email')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': (
            'login_id', 'password', 'name', 'period',
            'email', 'position', 'position_all', )
        }),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login_id', 'password1', 'password2', 'name', 'period', 'email')}
         ),
    )
    search_fields = ('email', 'name', )
    ordering = ('period',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
