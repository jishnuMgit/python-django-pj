from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'page-num'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'nextpage': self.get_next_link(),
            'previouspage': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })