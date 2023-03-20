from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=50)
    login = models.CharField(max_length=50)
    status = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('users-detail', kwargs={'id': self.id})
        return reverse('users-detail', args=[str(self.pk), ])


class Followed(models.Model):
    user = models.OneToOneField(on_delete=models.deletion.CASCADE, parent_link=True, primary_key=True, to='User')
    followers = models.ManyToManyField(to='User', related_name='followers')

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)


class Profile(models.Model):
    user = models.OneToOneField(on_delete=models.deletion.CASCADE, parent_link=True, primary_key=True, to='User')
    full_name = models.CharField(max_length=50)

    looking_for_a_job = models.BooleanField()
    looking_for_a_job_description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def get_absolute_url(self):
        # return reverse('users-detail', kwargs={'id': self.id})
        return reverse('profile-detail', args=[str(self.pk), ])


class Contacts(models.Model):
    user = models.OneToOneField(on_delete=models.deletion.CASCADE, parent_link=True, primary_key=True, to='User')
    github = models.CharField(max_length=50)
    vk = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    youtube = models.CharField(max_length=50)
    mainLink = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)


class Photo(models.Model):
    user = models.OneToOneField(on_delete=models.deletion.CASCADE, parent_link=True, primary_key=True, to='User')
    small = models.ImageField(upload_to='photos/%Y/%m/%d/small/')
    large = models.ImageField(upload_to='photos/%Y/%m/%d/large/')

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
