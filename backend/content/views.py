from rest_framework import generics
from .models import Navbar, Footer, Home, About, Skill, Project, ContactInfo, Certificate, Experience, Contact, Contactform, AboutHero, Education, CTA, ContactHero, ContactDetails, SkillHero, Formdetail, Softskills, Logo
from .serializers import (NavbarSerializers, FooterSerializers, HomeSerializers, AboutSerializers, SkillSerializers, ProjectSerializers, ContactInfoSerializers,
CertificateSerializers, ExperienceSerializers, ContactSerializers, ContactformSerializers, AboutHeroSerializers, EducationSerializers, CTASerializers, ContactHeroSerializers, ContactDetailsSerializers, SkillHeroSerializers, FormdetailSerializers, SoftskillsSerializers, LogoSerializers)


class LogoListCreateView(generics.ListCreateAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializers


class SoftskillsListCreateView(generics.ListCreateAPIView):
    queryset = Softskills.objects.all()
    serializer_class = SoftskillsSerializers




class FormdetailListCreateView(generics.ListCreateAPIView):
    queryset = Formdetail.objects.all()
    serializer_class = FormdetailSerializers


class SkillHeroListCreateView(generics.ListCreateAPIView):
    queryset = SkillHero.objects.all()
    serializer_class = SkillHeroSerializers



class ContactHeroListCreateView(generics.ListCreateAPIView):
    queryset = ContactHero.objects.all()
    serializer_class = ContactHeroSerializers

class ContactDetailsListCreateView(generics.ListCreateAPIView):
    queryset = ContactDetails.objects.all()
    serializer_class = ContactDetailsSerializers



class CTAListCreateView(generics.ListCreateAPIView):
    queryset = CTA.objects.all()
    serializer_class = CTASerializers


class EducationListCreateView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializers


class NavbarListCreateView(generics.ListCreateAPIView):
    queryset = Navbar.objects.all().order_by('order')
    serializer_class = NavbarSerializers


class FooterListCreateView(generics.ListCreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializers


class HomeListCreateView(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializers

class AboutListCreateView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializers

class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers

class ContactInfoListCreateView(generics.ListCreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializers

class CertificateListCreateView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializers

class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializers

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers

class ContactformListCreateView(generics.ListCreateAPIView):
    queryset = Contactform.objects.all()
    serializer_class = ContactformSerializers

class AboutHeroListCreateView(generics.ListCreateAPIView):
    queryset = AboutHero.objects.all()
    serializer_class = AboutHeroSerializers


def homepage(request):
    navbar_items = navbar.objects.all()
    footer_data = footer.objects.first()
    return render(request, 'index.html')


