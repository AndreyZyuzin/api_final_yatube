from rest_framework.pagination import LimitOffsetPagination, Response


class PostsPagination(LimitOffsetPagination):

    def get_paginated_response(self, data):
        print(self.request.query_params)
        if {'limit', 'offset'}.isdisjoint(self.request.query_params):
            return Response(data)
        return super().get_paginated_response(data)
