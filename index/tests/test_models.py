from django.test import TestCase
from index.models import Location, Category, Image
from index.views import locations


class LocationTestClass(TestCase):
    """
    test instance,saving,deleting,updating
    """

    def setUp(self):
        self.test_location = Location(location="Mali")

    def test_instance(self):
        self.assertTrue(isinstance(self.test_location, Location))

    def test_saving_location(self):
        self.test_location.save_locations()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_deleting_locations(self):
        self.test_location = Location(location="ichiraku")
        self.test_location.save_locations()
        self.test_location.delete_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations) < 1)

    def test_updating_image(self):
        self.test_location = Location(location="libashire")
        self.test_location.save_locations()
        updated = Location.update_location("soya park", "parleys")
        self.assertTrue(updated, "ichiraku")


class CategoryTestClass(TestCase):
    """
    test instance,saving,deleting,updating
    """

    def setUp(self):
        self.test = Category(name="dmc")

    def test_instance(self):
        self.assertTrue(isinstance(self.test, Category))

    def test_saving_category(self):
        self.test.save_category()
        images = Category.objects.all()
        self.assertTrue(len(images) > 0)

    def test_deleting_category(self):
        self.test.save_category()
        self.test.delete_category()
        locations = Category.objects.all()
        self.assertTrue(len(locations) < 1)

    def test_updating_category(self):
        self.test.save_category()
        updated = Category.update_category("naruto", 'dmc')
        self.assertTrue(updated, 'naruto')


class ImageTestClass(TestCase):
    def setUp(self):
        self.test_location = Location(location="Mali")
        self.test_location.save()
        # Category
        self.test_category = Category(name="ichiraku")
        self.test_category.save()

    def test_instance(self):
        self.test_image = Image(image="testImage",
                                image_url="testImage_url",
                                image_name="Test",
                                description="test",
                                location=self.test_location)
        self.test_image.save()
        self.test_image.category.add(self.test_category)
        self.assertTrue(isinstance(self.test_image, Image))

    def test_saving_image(self):
        images0 = Image.objects.all()
        len1 = len(images0)

        self.test_image = Image(image="testImage",
                                image_url="testImageurl",
                                image_name="Test",
                                description="test",
                                location=self.test_location)
        self.test_image.save()
        self.test_image.category.add(self.test_category)

        images1 = Image.objects.all()
        len2 = len(images1)

        self.assertTrue(len2 > len1)

    def test_deleting_image(self):
        self.test_image = Image(image="testImage",
                                image_url="testImage_url",
                                image_name="Test",
                                description="test",
                                location=self.test_location)
        self.test_image.save()
        self.test_image.category.add(self.test_category)
        images0 = Image.objects.all()
        len1 = len(images0)
        self.test_image.delete_image()
        images1 = Image.objects.all()
        len2 = len(images1)
        self.assertTrue(len1 > len2)
