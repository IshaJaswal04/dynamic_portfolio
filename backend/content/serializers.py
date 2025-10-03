from rest_framework import serializers
from .models import (
    Navbar, Footer, Home, About, Skill, Project, ContactInfo, Certificate,
    Experience, Contact, Contactform, AboutHero, Education, CTA, ContactHero,
    ContactDetails, SkillHero, Formdetail, Softskills, Logo
)

# ✅ Helper Mixin for Image URLs
class AbsoluteImageUrlMixin:
    def get_image_url(self, obj, field_name):
        request = self.context.get("request")
        field = getattr(obj, field_name)
        if field:
            return request.build_absolute_uri(field.url)
        return None


class LogoSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Logo
        fields = "__all__"

    def get_image(self, obj):
        return self.get_image_url(obj, "image")


class SoftskillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Softskills
        fields = '__all__'


class FormdetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Formdetail
        fields = '__all__'


class SkillHeroSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = SkillHero
        fields = '__all__'

    def get_image(self, obj):
        return self.get_image_url(obj, "image")


class ContactHeroSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ContactHero
        fields = '__all__'

    def get_image(self, obj):
        return self.get_image_url(obj, "image")


class ContactDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = '__all__'


class CTASerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CTA
        fields = '__all__'

    def get_image(self, obj):
        return self.get_image_url(obj, "image")


class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class AboutHeroSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = AboutHero
        fields = '__all__'

    def get_image(self, obj):
        return self.get_image_url(obj, "image")


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


class FooterSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = Footer
        fields = '__all__'

    def get_icon(self, obj):
        return self.get_image_url(obj, "icon")


class HomeSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Home
        fields = '__all__'

    def get_image(self, obj):
        return self.get_image_url(obj, "image")


class AboutSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = '__all__'

    def get_image(self, obj):
        return self.get_image_url(obj, "image")


class SkillSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = '__all__'

    def get_image(self, obj):
        return self.get_image_url(obj, "image")


class ProjectSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_image(self, obj):
        return self.get_image_url(obj, "image")


class ContactInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class CertificateSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = '__all__'

    def get_image(self, obj):
        return self.get_image_url(obj, "image")


class ExperienceSerializers(serializers.ModelSerializer, AbsoluteImageUrlMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = '__all__'

    def get_image(self, obj):
        return self.get_image_url(obj, "image")
