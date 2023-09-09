from django.test import TestCase
from .models import CollectionInfo
import pandas


# Create your tests here.

class CollectionTestCase(TestCase):
    def __int__(self):
        print("init")
    # def set_up(self):
    #     # data = CollectionInfo.objects.get(id=1)
    #     # print(data)
    #     # print(data.keys())
    #     print("hellow")

    def setUp(self):
        print("setUp")