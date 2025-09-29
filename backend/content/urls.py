from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),

    path('navbar/',views.NavbarListCreateView.as_view(),name = 'navbar-list'),
    path('footer/',views.FooterListCreateView.as_view(),name = 'footer-list'),
    path('home/',views.HomeListCreateView.as_view(),name = 'home-list'),
    path('about/',views.AboutListCreateView.as_view(),name = 'about-list'),
    path('skill/',views.SkillListCreateView.as_view(),name = 'skill-list'),
    path('contactinfo/',views.ContactInfoListCreateView.as_view(),name = 'contactinfo-list'),
    path('project/',views.ProjectListCreateView.as_view(),name = 'project-list'),
    path('certificate/',views.CertificateListCreateView.as_view(),name = 'certificate-list'),
    path('experience/',views.ExperienceListCreateView.as_view(),name = 'experience-list'),
    path('contact/',views.ContactListCreateView.as_view(), name = 'contact-list'),
    path('contactform/',views.ContactformListCreateView.as_view(), name = 'contactform-list'),
    path('abouthero/',views.AboutHeroListCreateView.as_view(), name = 'abouthero-list'),
    path('education/',views.EducationListCreateView.as_view(), name = 'education-list'),
    path('cta/',views.CTAListCreateView.as_view(), name = "cta-list"),
    path('contacthero/',views.ContactHeroListCreateView.as_view(), name = "contacthero-list"),
    path('contactdetails/',views.ContactDetailsListCreateView.as_view(), name = "contactdetails-list"),
    path('skillhero/',views.SkillHeroListCreateView.as_view(), name = "skillhero-list"),
    path('formdetail/',views.FormdetailListCreateView.as_view(), name = "formdetail-list"),
    path('softskills/',views.SoftskillsListCreateView.as_view(), name = "softskills-list"),
    path('logo/',views.LogoListCreateView.as_view(), name = "logo"),
   
]

