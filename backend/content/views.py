from rest_framework import generics
from .models import (
    Navbar, Footer, Home, About, Skill, Project, ContactInfo, Certificate, Experience,
    Contact, Contactform, AboutHero, Education, CTA, ContactHero, ContactDetails,
    SkillHero, Formdetail, Softskills, Logo
)
from .serializers import (
    NavbarSerializers, FooterSerializers, HomeSerializers, AboutSerializers,
    SkillSerializers, ProjectSerializers, ContactInfoSerializers, CertificateSerializers,
    ExperienceSerializers, ContactSerializers, ContactformSerializers, AboutHeroSerializers,
    EducationSerializers, CTASerializers, ContactHeroSerializers, ContactDetailsSerializers,
    SkillHeroSerializers, FormdetailSerializers, SoftskillsSerializers, LogoSerializers
)


# 🔹 Base view that injects request context
class BaseListCreateView(generics.ListCreateAPIView):
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class LogoListCreateView(BaseListCreateView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializers


class SoftskillsListCreateView(BaseListCreateView):
    queryset = Softskills.objects.all()
    serializer_class = SoftskillsSerializers


class FormdetailListCreateView(BaseListCreateView):
    queryset = Formdetail.objects.all()
    serializer_class = FormdetailSerializers


class SkillHeroListCreateView(BaseListCreateView):
    queryset = SkillHero.objects.all()
    serializer_class = SkillHeroSerializers


class ContactHeroListCreateView(BaseListCreateView):
    queryset = ContactHero.objects.all()
    serializer_class = ContactHeroSerializers


class ContactDetailsListCreateView(BaseListCreateView):
    queryset = ContactDetails.objects.all()
    serializer_class = ContactDetailsSerializers


class CTAListCreateView(BaseListCreateView):
    queryset = CTA.objects.all()
    serializer_class = CTASerializers


class EducationListCreateView(BaseListCreateView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializers


class NavbarListCreateView(BaseListCreateView):
    queryset = Navbar.objects.all().order_by('order')
    serializer_class = NavbarSerializers


class FooterListCreateView(BaseListCreateView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializers


class HomeListCreateView(BaseListCreateView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializers


class AboutListCreateView(BaseListCreateView):
    queryset = About.objects.all()
    serializer_class = AboutSerializers


class SkillListCreateView(BaseListCreateView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers


class ProjectListCreateView(BaseListCreateView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers


class ContactInfoListCreateView(BaseListCreateView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializers


class CertificateListCreateView(BaseListCreateView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializers


class ExperienceListCreateView(BaseListCreateView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializers


class ContactListCreateView(BaseListCreateView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


class ContactformListCreateView(BaseListCreateView):
    queryset = Contactform.objects.all()
    serializer_class = ContactformSerializers


class AboutHeroListCreateView(BaseListCreateView):
    queryset = AboutHero.objects.all()
    serializer_class = AboutHeroSerializers


def homepage(request):
    navbar_items = navbar.objects.all()
    footer_data = footer.objects.first()
    return render(request, 'index.html')


