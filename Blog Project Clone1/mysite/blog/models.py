from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

# Model for Posting blogs
class Post(models.Model):
    # field of the author
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_= models.DateTimeField(deafult=timezone.now())
    publish_date = models.DateTimeField(blank=True,null=True)

     # a method to be called to publish a written post
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    # a method to approve comments written in a post
    def approved_comments(self):
        return self.comments.filter(approved_comment = True)

    # a method for returning to the post detail view we just created
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})    

    # a special method for string representation of the object
    def __str__(self):
        return self.title 

# A class for comments in the post

class Comment(models.Model):
    # foriegn key to access the post 
    post = models.ForeignKey('blog.Post',related_name="comments")
    
    # field for the comments on the post
    auth = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)


    # a method for approve
    def approve(self):
        self.approved_comment = True
        self.save() 

    # a method for returning to the post detail view we just created
    def get_absolute_url(self):
        return reverse('post_list')

    # a special method for string representation of the object-comment"
    def __str__(self):
        return self.text


        


    
