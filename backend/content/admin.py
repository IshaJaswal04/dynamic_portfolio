from django.contrib import admin
from .models import Navbar, Footer, Home, About, Skill, Project, ContactInfo, Experience, Certificate, Contact, Contactform, AboutHero, Education, CTA, ContactHero, ContactDetails, SkillHero, Formdetail, Softskills, Logo


admin.site.register(Navbar)
class navbarAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'order', 'is_active')
    list_editable = ('link', 'order', 'is_active')
    ordering = ('order',)


admin.site.register(Footer)
class footerAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'order', 'is_active')
    list_editable = ('link', 'order', 'is_active')
    ordering = ('order',)

admin.site.register(Contact)
admin.site.register(Home)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ContactInfo)
admin.site.register(Experience)
admin.site.register(Certificate)
admin.site.register(Contactform)
admin.site.register(AboutHero)
admin.site.register(Education)
admin.site.register(CTA)
admin.site.register(ContactHero)
admin.site.register(ContactDetails)
admin.site.register(SkillHero)
admin.site.register(Formdetail)
admin.site.register(Softskills)
admin.site.register(Logo)

