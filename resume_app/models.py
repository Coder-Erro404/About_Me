from django.db import models

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     F_name= models.CharField(max_length=255)
     L_name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "Message from " + self.F_name + ' - ' + self.email

class addblog(models.Model):
     sno= models.AutoField(primary_key=True)
     p_name= models.CharField(max_length=255)
     author= models.CharField(max_length=225)
     content= models.TextField()
     Decri= models.CharField(max_length=255)
     p_url= models.CharField(max_length=255)
     Img = models.ImageField(upload_to='add_images')
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "Project_Name"+ " :  "+ self.p_name 

class Notes(models.Model):
     sno= models.AutoField(primary_key=True)
     header= models.CharField(max_length=500)
     Author= models.CharField(max_length=255)
     content= models.TextField()
     p_url= models.CharField(max_length=255)
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "header"+ " :  "+ self.header 
