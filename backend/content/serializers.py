from rest_framework import serializers
from .models import (
    Navbar, Footer, Home, About, Skill, Project, ContactInfo, Certificate, Experience,
    Contact, Contactform, AboutHero, Education, CTA, ContactHero, ContactDetails,
    SkillHero, Formdetail, Softskills, Logo
)

# Utility function for Cloudinary URL fields
def get_cloudinary_url(field):
    if field:
        return field.url
    return None


class LogoSerializers(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Logo
        fields = "__all__"

    def get_logo(self, obj):
        return get_cloudinary_url(obj.logo)


class SoftskillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Softskills
        fields = '__all__'


class FormdetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Formdetail
        fields = '__all__'


class SkillHeroSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = SkillHero
        fields = '__all__'

    def get_image(self, obj):
        return get_cloudinary_url(obj.image)


class ContactHeroSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ContactHero
        fields = '__all__'

    def get_image(self, obj):
        return get_cloudinary_url(obj.image)


class ContactDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = '__all__'


class CTASerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    resume = serializers.SerializerMethodField()

    class Meta:
        model = CTA
        fields = '__all__'

    def get_image(self, obj):
        return get_cloudinary_url(obj.image)

    def get_resume(self, obj):
        return get_cloudinary_url(obj.resume)


class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class AboutHeroSerializers(serializers.ModelSerializer):
    background_image = serializers.SerializerMethodField()

    class Meta:
        model = AboutHero
        fields = '__all__'

    def get_background_image(self, obj):
        return get_cloudinary_url(obj.background_image)


class ContactformSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contactform
        fields = '__all__'


class ContactSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = '__all__'

    def get_image(self, obj):
        return get_cloudinary_url(obj.image)


class NavbarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'


class FooterSerializers(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()
    icon2 = serializers.SerializerMethodField()

    class Meta:
        model = Footer
        fields = '__all__'

    def get_icon(self, obj):
        return get_cloudinary_url(obj.icon)

    def get_icon2(self, obj):
        return get_cloudinary_url(obj.icon2)


class HomeSerializers(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()
    background_image = serializers.SerializerMethodField()

    class Meta:
        model = Home
        fields = '__all__'

    def get_profile_image(self, obj):
        return get_cloudinary_url(obj.profile_image)

    def get_background_image(self, obj):
        return get_cloudinary_url(obj.background_image)


class AboutSerializers(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()
    background_image = serializers.SerializerMethodField()
    git_image = serializers.SerializerMethodField()
    lin_image = serializers.SerializerMethodField()
    resume = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = '__all__'

    def get_profile_image(self, obj):
        return get_cloudinary_url(obj.profile_image)

    def get_background_image(self, obj):
        return get_cloudinary_url(obj.background_image)

    def get_git_image(self, obj):
        return get_cloudinary_url(obj.git_image)

    def get_lin_image(self, obj):
        return get_cloudinary_url(obj.lin_image)

    def get_resume(self, obj):
        return get_cloudinary_url(obj.resume)


class SkillSerializers(serializers.ModelSerializer):
    background_image = serializers.SerializerMethodField()
    logo1 = serializers.SerializerMethodField()
    logo2 = serializers.SerializerMethodField()
    logo3 = serializers.SerializerMethodField()
    logo4 = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = '__all__'

    def get_background_image(self, obj):
        return get_cloudinary_url(obj.background_image)

    def get_logo1(self, obj):
        return get_cloudinary_url(obj.logo1)

    def get_logo2(self, obj):
        return get_cloudinary_url(obj.logo2)

    def get_logo3(self, obj):
        return get_cloudinary_url(obj.logo3)

    def get_logo4(self, obj):
        return get_cloudinary_url(obj.logo4)


class ProjectSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_image(self, obj):
        return get_cloudinary_url(obj.image)


class ContactInfoSerializers(serializers.ModelSerializer):
    linkedin_icon = serializers.SerializerMethodField()
    github_icon = serializers.SerializerMethodField()
    contact_image = serializers.SerializerMethodField()

    class Meta:
        model = ContactInfo
        fields = '__all__'

    def get_linkedin_icon(self, obj):
        return get_cloudinary_url(obj.linkedin_icon)

    def get_github_icon(self, obj):
        return get_cloudinary_url(obj.github_icon)

    def get_contact_image(self, obj):
        return get_cloudinary_url(obj.contact_image)


class CertificateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class ExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

