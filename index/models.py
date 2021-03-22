from django.db import models
import datetime as dt


class Location(models.Model):
    """
    Image location model
    """
    PLACES = (
        ("Mali", "Mali"),
        ("ichiraku", "ichiraku"),
        ("leaf village", "leaf village"),
        "soya park, soya park",
        "libashire, libashire",
        "Parleys, parleys"
    )
    location = models.CharField(max_length=140, choices=PLACES)

    def save_locations(self):
        self.save()

    def delete_locations(self):
        self.delete()

    @classmethod
    def update_location(cls, place, update):
        updated = cls.objects.filter(location=place).update(location=update)
        return updated

    def __str__(self):
        return self.location


class Category(models.Model):
    """
    Image category model
    """
    CATEGORIES = (
        ("naruto", "dmc"),
        ("dmc", "naruto")
    )
    name = models.CharField(max_length=120, choices=CATEGORIES)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, cat, update):
        updated = cls.objects.filter(name=cat).update(name=update)
        return updated

    def __str__(self):
        return self.name


class Image(models.Model):
    """
    Image model
    """
    image = models.ImageField(upload_to='gallery/', blank=True)
    image_url = models.TextField(blank=False)
    image_name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=100, blank=False)
    category = models.ManyToManyField('Category', blank=True)
    post_date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-post_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, update):
        updated = cls.objects.filter(id=id).update(target=update)
        return updated

    @classmethod
    def get_all(cls):
        images = cls.objects.order_by('-post_date')
        return images

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def searched(cls, query):
        result = cls.objects.filter(
            description__icontains=query).order_by('-post_date')
        return result

    @classmethod
    def today_pics(cls):
        today = dt.date.today()
        images = cls.objects.filter(post_date__date=today)
        return images

    @classmethod
    def filter_location(cls, place):
        images = cls.objects.filter(
            location__location__startswith=place).order_by('-post_date')
        return images

    @classmethod
    def filter_category(cls, query):
        images = cls.objects.filter(
            category__name__startswith=query).order_by('-post_date')
        return images
