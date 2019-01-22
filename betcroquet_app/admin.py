from django.contrib import admin
from betcroquet_app.models import BetCollection,BetTemplate,Bet, Category,CategoryWinner, BetSelection,Option
# Register your models here.
admin.site.register(Bet)
admin.site.register(Category)
admin.site.register(Option)
admin.site.register(BetCollection)
admin.site.register(CategoryWinner)
admin.site.register(BetTemplate)
admin.site.register(BetSelection)
