from django.contrib import admin
from .models import Book, Author

#Customising the admin page.Example
# class BooksAdmin(admin.ModelAdmin):        
#     list_display = ('id','name','age','nationality') #for displaying more values as columns
#     list_filter = ('age','nationality') #for filtering

# admin.site.register(Books,BooksAdmin)

admin.site.register(Book)
admin.site.register(Author)
