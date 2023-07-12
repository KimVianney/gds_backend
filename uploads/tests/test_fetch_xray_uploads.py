from base_test.base_test import BaseTestCase


class FetchXrayUploadsTestCase(BaseTestCase):

    def test_fetch_xray_uploads(self):
        """Test fetching a users xray uploads"""
        results = self.create_xray_upload(self.xray_upload, self.user_data)

        url = '/uploads/'

        self.client.force_authenticate(user=results['user'])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)

    def test_fetch_xray_uploads_not_authenticated(self):
        """Test fetching a users xray uploads when not logged in"""
        self.create_xray_upload(self.xray_upload, self.user_data)

        url = '/uploads/'

        self.client.force_authenticate(user=None)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 401)
