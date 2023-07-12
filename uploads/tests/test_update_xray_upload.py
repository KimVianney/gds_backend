from base_test.base_test import BaseTestCase


class UpdateXrayUploadTestCase(BaseTestCase):

    def test_update_xray_upload(self):
        """Test updating xray upload"""
        result = self.create_xray_upload(self.xray_upload, self.user_data)

        url = f"/uploads/{result['upload'].id}/"

        self.client.force_authenticate(user=result['user'])
        response = self.client.patch(
            url, data=self.update_xray_upload, format='json')

        self.assertEqual(response.status_code, 200)

    def test_update_xray_upload_invalid_request(self):
        """Test updating xray upload with invalid request body"""
        result = self.create_xray_upload(self.xray_upload, self.user_data)

        url = f"/uploads/{result['upload'].id}/"

        self.client.force_authenticate(user=result['user'])
        response = self.client.patch(url, data={}, format='json')

        self.assertEqual(response.status_code, 400)

    def test_update_xray_upload_not_authenticated(self):
        """Test updating xray upload not logged in"""
        result = self.create_xray_upload(self.xray_upload, self.user_data)

        url = f"/uploads/{result['upload'].id}/"

        response = self.client.patch(
            url, data=self.update_user_data, format='json')

        self.assertEqual(response.status_code, 401)

    def test_update_xray_upload_not_owner(self):
        """Test updating xray upload when not the owner"""
        result = self.create_xray_upload(self.xray_upload, self.user_data)
        result2 = self.create_xray_upload(
            self.other_xray_upload, self.other_user_data)

        url = f"/uploads/{result['upload'].id}/"

        self.client.force_authenticate(user=result2['user'])
        response = self.client.patch(
            url, data=self.update_user_data, format='json')

        self.assertEqual(response.status_code, 403)
