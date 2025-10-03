from rest_framework import serializers
from .models import Navbar, Footer, Home, About, Skill, Project, ContactInfo, Certificate, Experience, Contact, Contactform, AboutHero, Education, CTA, ContactHero, ContactDetails, SkillHero, Formdetail, Softskills, Logo


class LogoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"


class SoftskillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Softskills
        fields = '__all__'




class FormdetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Formdetail
        fields = '__all__'


class SkillHeroSerializers(serializers.ModelSerializer):
    class Meta:
        model = SkillHero
        fields = '__all__'


class ContactHeroSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactHero
        fields = '__all__'

class ContactDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = '__all__'




class CTASerializers(serializers.ModelSerializer):
    class Meta:
        model = CTA
        fields = '__all__'


class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class AboutHeroSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutHero
        fields = '__all__'


class ContactformSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contactform
        fields = '__all__'

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'  

class NavbarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'

class FooterSerializers(serializers.ModelSerializer):
    icon = serializers.ImageField(use_url=True) 
    class Meta:
        model = Footer
        fields = '__all__'

class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ContactInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class CertificateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class ExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'