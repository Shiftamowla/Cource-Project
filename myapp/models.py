from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
    USER=[
        ('creator','Creator'),
        ('viewer','Viewer')
    ]

    usertype=models.CharField(choices=USER,max_length=100,null=True)
    Image=models.ImageField(upload_to='Media/user_Pic',null=True)


    def  __str__(self):
        return f"{self.username}-{self.usertype}"
    
class viewerProfileModel(models.Model):
    user=models.OneToOneField(Custom_user,on_delete=models.CASCADE,related_name='viewersProfile', null=True)
    
    def __str__(self):
        return f"{self.user.username}"   
    
class CreatorProfileModel(models.Model):
    user = models.OneToOneField(Custom_user, on_delete=models.CASCADE,related_name='creatorProfile', null=True)
    
    def __str__(self):
        return f"{self.user.username}"
    

    
class Category_model(models.Model):
    name = models.CharField(max_length=255, null=True)
    Icon = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.name}"
    

    
class author_profile(models.Model):
    course = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    name = models.CharField(max_length=255, null=True)
    about_author = models.TextField(max_length=1000,null=True)
    Image=models.ImageField(upload_to='Media/author_Pic',null=True)
    detailed_bio = models.TextField(null=True, blank=True)
    experience = models.PositiveIntegerField(default=0)  # Years of experience
    field_of_expertise = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    social_link = models.URLField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
    
class CourseModel(models.Model):
    STATUS = [
        ('publish', 'PUBLISH'),
        ('draft', 'DRAFT'),
    ]

    Author = models.ForeignKey(author_profile, on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category_model, on_delete=models.CASCADE,null=True)
    Course_title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=1000,null=True)
    Price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(max_length=10,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True,null=True)
    status = models.CharField(choices=STATUS,max_length=255, null=True)
    featured_image=models.ImageField(upload_to='Media/Course_Pic',null=True)
    featured_video=models.CharField(max_length=200,null=True)
    def __str__(self):
        return f"{self.Course_title}"
    
    def allcategory(self):
        return CourseModel.objects.all()



class Lesson(models.Model):

    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE,null=True)

    name = models. CharField (max_length=200)

    def __str__(self):
        return f"{self.id}-{self.course}-{self.name}"


class Video (models.Model):

        serial_number = models. IntegerField (null=True)

        thumbnail = models. ImageField (upload_to="Media/Yt_Thumbnail", null=True)

        course = models.ForeignKey(CourseModel, on_delete=models.CASCADE,null=True)

        lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,null=True)

        title=models.CharField(max_length=100)

        youtube_id = models.CharField (max_length=200)

        time_duration = models. FloatField(null=True)

        preview = models. BooleanField (default=False)


        def __str__(self):
            return f"{self.title}"
        
class CourseeeModel(models.Model):

    Author = models.ForeignKey(author_profile, on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category_model, on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE,null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.course}"
    
class author(models.Model):

    Author = models.ForeignKey(author_profile, on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category_model, on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.Author}-{self.course}"
    
class only1(models.Model):

    Author = models.ForeignKey(author, on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f"{self.Author}-{self.course}"