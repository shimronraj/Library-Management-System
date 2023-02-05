from django.contrib import admin
from .models import userlogin, student_details,admin_details,book_details,book_lend_details,fine_details

# Register your models here.
admin.site.register(userlogin)
admin.site.register(student_details)
admin.site.register(admin_details)
admin.site.register(book_details)
admin.site.register(book_lend_details)
admin.site.register(fine_details)


