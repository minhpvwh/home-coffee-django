from django.contrib import admin
from homecoffee.models import ReviewCustomer


# Register your models here.

class ReviewCustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_job', 'rating')
    search_fields = ('customer_name',)


admin.site.register(ReviewCustomer, ReviewCustomerAdmin)
