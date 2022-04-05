from rest_framework.pagination import (CursorPagination, LimitOffsetPagination,
                                       PageNumberPagination)


class WatchListPagination(PageNumberPagination):
    page_size = 2                   # Defined page size.
    page_query_param='pagina'       # Query param name to pagination.
    page_size_query_param = 'size'  # Custom field to find how many elements you want.
    max_page_size = 6               # You set a limit to data you client can consume.
    last_page_strings = 'end'


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 4
    max_limit = 8
    limit_query_param='limit'
    offset_query_param='start'


class WatchListCPagination(CursorPagination):
    page_size = 5
