from rest_framework import serializers
from .models import (
    Navbar, Footer, Home, About, Skill, Project, ContactInfo, Certificate, Experience,
    Contact, Contactform, AboutHero, Education, CTA, ContactHero, ContactDetails,
    SkillHero, Formdetail, Softskills, Logo
)

# 🔹 Base serializer that fixes media URLs
class AbsoluteUrlModelSerializer(serializers.ModelSerializer):
    """
    Ensures that all FileField / ImageField return absolute URLs.
    """
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get("request")

        for field_name, field_value in representation.items():
            field = self.fields.get(field_name)
            if field and isinstance(field, (serializers.ImageField, serializers.FileField)):
                if field_value and request:
                    representation[field_name] = request.build_absolute_uri(field_value)
        return representation


class LogoSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"


class SoftskillsSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Softskills
        fields = '__all__'


class FormdetailSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Formdetail
        fields = '__all__'


class SkillHeroSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = SkillHero
        fields = '__all__'


class ContactHeroSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = ContactHero
        fields = '__all__'


class ContactDetailsSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = ContactDetails
        fields = '__all__'


class CTASerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = CTA
        fields = '__all__'


class EducationSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class AboutHeroSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = AboutHero
        fields = '__all__'


class ContactformSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Contactform
        fields = '__all__'


class ContactSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class NavbarSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'


class FooterSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


class HomeSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class AboutSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class SkillSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ContactInfoSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class CertificateSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class ExperienceSerializers(AbsoluteUrlModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
