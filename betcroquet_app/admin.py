from django.contrib import admin
from betcroquet_app.models import BetCollection,Bet, Category,CategoryWinner, Option
# Register your models here.
admin.site.register(Bet)
admin.site.register(Category)
admin.site.register(Option)
admin.site.register(BetCollection)
admin.site.register(CategoryWinner)
