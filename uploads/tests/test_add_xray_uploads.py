from base_test.base_test import BaseTestCase


class CreateImageUploadsTestCase(BaseTestCase):

    def test_creating_image_upload(self):
        """Test creating an image upload"""
        user = self.create_user(self.user_data)

        url = '/uploads/'

        self.client.force_authenticate(user=user)
        response = self.client.post(url, data=self.image_upload, format='json')

        self.assertEqual(response.status_code, 201)

    def test_creating_image_upload_invalid_data(self):
        """Test creating an upload with invalid request body"""
        user = self.create_user(self.user_data)

        url = '/uploads/'

        self.client.force_authenticate(user=user)
        response = self.client.post(
            url, data=self.invalid_image_upload, format='json')

        self.assertEqual(response.status_code, 400)

    def test_creating_image_upload_not_authenticated(self):
        """Test creating an xray upload when not logged in"""
        self.create_user(self.user_data)

        url = '/uploads/'

        response = self.client.post(url, data=self.image_upload, format='json')
        self.assertEqual(response.status_code, 401)
