from rest_framework import pagination


class ImageUploadPagination(pagination.PageNumberPagination):

    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'

    def get_paginated_response(self, data):
        return {
            'message': 'Done',
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'uploads': data
        }