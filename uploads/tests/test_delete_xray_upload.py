from base_test.base_test import BaseTestCase


class DeleteXrayUploadTestCase(BaseTestCase):

    def test_delete_xray_upload(self):
        """Test deleting xray upload"""
        result = self.create_xray_upload(self.xray_upload, self.user_data)

        url = f"/uploads/{result['upload'].id}/"

        self.client.force_authenticate(user=result['user'])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 200)

    def test_delete_xray_upload_invalid_id(self):
        """Test deleting xray upload with invalid ID"""
        result = self.create_xray_upload(self.xray_upload, self.user_data)

        url = "/uploads/0/"

        self.client.force_authenticate(user=result['user'])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 400)

    def test_delete_xray_upload_not_authenticated(self):
        """Test deleting xray upload not logged in"""
        result = self.create_xray_upload(self.xray_upload, self.user_data)

        url = f"/uploads/{result['upload'].id}/"

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 401)

    def test_delete_xray_upload_not_owner(self):
        """Test deleting xray upload not owner"""
        result = self.create_xray_upload(self.xray_upload, self.user_data)
        result2 = self.create_xray_upload(
            self.other_xray_upload, self.other_user_data)

        url = f"/uploads/{result['upload'].id}/"

        self.client.force_authenticate(user=result2['user'])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 403)
