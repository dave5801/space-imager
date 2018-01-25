from django.test import TestCase

from space_imager_profile.models import Create_A_New_Space_Photo_from_NASA_API


class TestNASA_API_Call_and_json_response(TestCase):

    def test_json_response_is_correct(self):
        test_get_newly_created_photo = Create_A_New_Space_Photo_from_NASA_API()
        assert self.assertIsNotNone(test_get_newly_created_photo)

