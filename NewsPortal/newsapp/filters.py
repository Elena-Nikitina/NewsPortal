from django_filters import FilterSet, DateFromToRangeFilter
from .models import Post
from django_filters.widgets import RangeWidget


class PostFilter(FilterSet):
    dateCreation = DateFromToRangeFilter(
        label='Date creation',
        lookup_expr='gt',
        widget=RangeWidget(attrs={'type': 'date'}))


    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'text': ['icontains'],
        }

        # author = ModelChoiceFilter(
        #     field_name='author'


# from django_filters import FilterSet
# from .models import Product
#
#
# class ProductFilter(FilterSet):
#    class Meta:
#        model = Product
#        fields = {
#            'name': ['icontains'],
#            'quantity': ['gt'],
#            'price': [
#                'lt',
#            ],
#        }