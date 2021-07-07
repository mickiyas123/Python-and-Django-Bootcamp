from django.db import models
from django.utils import timezone
from django.urls import reverse 

# Create your models here.

# class for writing,saving and posting content on the blog.
class Post(models.model):
    # superuser is the author
    author = models.ForeignKey('auth.User')
   
    # the title for the content, content for the post
    title = models.CharField(max_length=200)
    text = models.TextField()
   
    #the date for the created content and the date to be published
    create_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    
    # a method for saving the publish date of the content in time of publishing
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # a method for approving comments on the content of the post
    def approve_comment(self):
        return self.comments.filter(approved_comment=True)

    # a method for what django should do after creating the post
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':'self.pk'})    

    # a method for returning the title of post
    def __str__(self):
        return self.title 

# class for the comments
class Comment(models.Model):
    # to connect with the post class
    post = models.ForeignKey('blog.Post',related_name="comments")
    
    # author and text for the comment on the post
    author = models.CharField(max_length='200')
    text =  models.TextField()
    
    # the curent date for the comment 
    create_date = models.DateTimeField(default = timezone.now())
    
    # approving the comments with inital value false
    approved_comment = models.BooleanField(default=False)

    # a method for approved comment
    def approve(self):
        self.approved_comment = True
        self.save()

    # a method for going back to the home page after writing the post 
    def get_absolute_url(self):
        return reverse('post_list')    

    # a method for returning text of the comment    
    def __str__(self):
        return self.text





