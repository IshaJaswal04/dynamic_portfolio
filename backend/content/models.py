from django.db import models
from cloudinary.models import CloudinaryField

class Logo(models.Model):
    logo = CloudinaryField('logo', blank=True, null=True)

class Navbar(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Footer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    heading = models.CharField(max_length=30, null=True)
    heading2 = models.CharField(max_length=30, null=True)
    heading3 = models.CharField(max_length=30, null=True)
    Gitlink = models.CharField(max_length=100, null=True)
    Linkdinlink = models.CharField(max_length=100, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    icon = CloudinaryField('icon', blank=True, null=True)
    icon_desc = models.CharField(max_length=50, null=True)
    icon2 = CloudinaryField('icon2', blank=True, null=True)
    icon2_desc = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Home(models.Model):
    bigHeading = models.CharField(max_length=100, null=True)
    subHeading = models.CharField(max_length=200, null=True)
    Tagline = models.CharField(max_length=400, null=True)
    buttonText = models.CharField(max_length=50, null=True)
    profile_image = CloudinaryField('profile_image', blank=True, null=True)
    background_image = CloudinaryField('background_image', blank=True, null=True)

    def __str__(self):
        return self.bigHeading

class About(models.Model):
    title = models.CharField(max_length=100, null=True)
    subtitle = models.CharField(max_length=200, null=True)
    profile_image = CloudinaryField('profile_image', blank=True, null=True)
    background_image = CloudinaryField('background_image', blank=True, null=True)
    bio = models.TextField()
    bio1 = models.TextField(null=True)
    bio2 = models.TextField(null=True)
    bio3 = models.TextField(null=True)
    github_title = models.CharField(max_length=50, null=True)
    github = models.URLField(blank=True)
    git_image = CloudinaryField('git_image', blank=True, null=True)
    linkedin_title = models.CharField(max_length=50, null=True)
    linkedin = models.URLField(blank=True)
    lin_image = CloudinaryField('lin_image', blank=True, null=True)
    read = models.CharField(max_length=50, null=True)
    button_text = models.CharField(max_length=50, null=True)
    resume = CloudinaryField('resume', resource_type='raw', blank=True, null=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=100, blank=True)
    background_image = CloudinaryField('background_image', blank=True, null=True)
    one_name1 = models.CharField(max_length=100, blank=True)
    one_level1 = models.CharField(max_length=100, blank=True)
    one_name2 = models.CharField(max_length=100, blank=True)
    one_level2 = models.CharField(max_length=100, blank=True)
    one_name3 = models.CharField(max_length=100, blank=True)
    one_level3 = models.CharField(max_length=100, blank=True)
    one_name4 = models.CharField(max_length=100, blank=True)
    one_level4 = models.CharField(max_length=100, blank=True)
    one_name5 = models.CharField(max_length=100, blank=True)
    one_level5 = models.CharField(max_length=100, blank=True)
    logo1 = CloudinaryField('logo1', blank=True, null=True)

    category2 = models.CharField(max_length=100, blank=True)
    two_name1 = models.CharField(max_length=100, blank=True)
    two_level1 = models.CharField(max_length=100, blank=True)
    two_name2 = models.CharField(max_length=100, blank=True)
    two_level2 = models.CharField(max_length=100, blank=True)
    two_name3 = models.CharField(max_length=100, blank=True)
    two_level3 = models.CharField(max_length=100, blank=True)
    logo2 = CloudinaryField('logo2', blank=True, null=True)

    category3 = models.CharField(max_length=100, null=True)
    three_name1 = models.CharField(max_length=100, blank=True)
    three_level1 = models.CharField(max_length=100, blank=True)
    three_name2 = models.CharField(max_length=100, blank=True)
    three_level2 = models.CharField(max_length=100, blank=True)
    logo3 = CloudinaryField('logo3', blank=True, null=True)

    category4 = models.CharField(max_length=100, null=True)
    four_name1 = models.CharField(max_length=100, blank=True)
    four_level1 = models.CharField(max_length=100, blank=True)
    four_name2 = models.CharField(max_length=100, blank=True)
    four_level2 = models.CharField(max_length=100, blank=True)
    four_name3 = models.CharField(max_length=100, blank=True)
    four_level3 = models.CharField(max_length=100, blank=True)
    logo4 = CloudinaryField('logo4', blank=True, null=True)

    def __str__(self):
        return self.category

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin_icon = CloudinaryField('linkedin_icon', blank=True, null=True)
    github_icon = CloudinaryField('github_icon', blank=True, null=True)
    contact_image = CloudinaryField('contact_image', blank=True, null=True)

    def __str__(self):
        return self.full_name

class Contact(models.Model):
    heading = models.CharField(max_length=100, null=True)
    desc = models.TextField(null=True)
    tagline = models.CharField(max_length=50, null=True)
    button_Text = models.CharField(max_length=50, null=True)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.heading

class Contactform(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name or self.email or "No Name")

class Experience(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    contact = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, related_name='certificates')
    name = models.CharField(max_length=100)
    issuing_organisation = models.CharField(max_length=100)
    issue_date = models.DateField()

    def __str__(self):
        return self.name

class AboutHero(models.Model):
    background_image = CloudinaryField('background_image', blank=True, null=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.desc

class CTA(models.Model):
    text = models.CharField(max_length=100)
    button_text = models.CharField(max_length=50)
    image = CloudinaryField('image', blank=True, null=True)
    resume = CloudinaryField('resume', resource_type='raw', blank=True, null=True)

class ContactHero(models.Model):
    image = CloudinaryField('image', blank=True, null=True)
    title = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.desc

class ContactDetails(models.Model):
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

class SkillHero(models.Model):
    image = CloudinaryField('image', blank=True, null=True)
    tagline = models.TextField(blank=True)
    item1 = models.CharField(max_length=50, blank=True)
    item2 = models.CharField(max_length=50, blank=True)
    item3 = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.item1

class Formdetail(models.Model):
    h3 = models.CharField(max_length=100, blank=True)
    p = models.TextField(blank=True)

    def __str__(self):
        return self.h3

class Softskills(models.Model):
    title = models.CharField(max_length=50, blank=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.title
