from django.test import TestCase
from .models import Tree
from .searching import search_for_tree


# Create your tests here.
class TreeTestCase(TestCase):
    def setUp(self):
        Tree.objects.create(
            name='tree',
            url='nothing',
            type='fruit',
            soil='H',
            sun='L',
            food='M',
            water='L',
            pruning='M',
            max_height=4,
            growth_rate='H',
            price=10000,
        )
        Tree.objects.create(
            name='other',
            url='nothing',
            type='nznative',
            soil='L',
            sun='M',
            food='M',
            water='M',
            pruning='H',
            max_height=1,
            growth_rate='H',
            price=20000,
        )

    def test_can_search_by_name(self):
        """
        Test to see if you can search the database by name
        :return: List of Tree objects as the query results.
        """

        tree1 = search_for_tree('tree', {})[0]
        tree2 = search_for_tree('other', {})[0]

        self.assertEqual(tree1.price, 10000)
        self.assertEqual(tree1.type, 'fruit')

        self.assertEqual(tree2.price, 20000)
        self.assertEqual(tree2.type, 'nznative')

    def test_can_filter_by_type(self):
        results1 = search_for_tree('r', {'type': 'fruit'})[0]
        results2 = search_for_tree('r', {'type': 'nznative'})[0]

        self.assertEqual(results1.type, 'fruit')
        self.assertEqual(results2.type, 'nznative')

    def test_can_filter_multiple_types(self):
        results = search_for_tree('r', {'soil': 'L', 'sun': 'M'})[0]

        self.assertEqual(results.soil, 'L')
        self.assertEqual(results.sun, 'M')
    