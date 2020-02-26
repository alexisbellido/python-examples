import unittest
from store import Store

if __name__ == "__main__":

    Store.set('name', 'Mike')

    # TODO update the tests values

    class TestStore(unittest.TestCase):

        def test_set(self):
            Store.set('name', 'Mike')
            self.assertIn('name', Store._store.keys())
            self.assertEqual('Mike', Store._store.get('name')[0])

            Store.set('name', 'Joe')
            self.assertIn('name', Store._store.keys())
            self.assertEqual('Joe', Store._store.get('name')[0])

            Store.set(key='name', value='Mike', duration=30)
            self.assertIn('name', Store._store.keys())
            self.assertEqual('Mike', Store._store.get('name')[0])

            # Check that it won't accept a non-numeric duration
            with self.assertRaises(TypeError):
                Store.set(key='name', value='Mike', duration='x')

        def test_get(self):
            Store.set('name', 'Mike')
            self.assertEqual('Mike', Store.get('name'))

            Store.set(key='name', value='Mike', duration=30)
            self.assertEqual('Mike', Store.get('name'))

            Store.set(key='country', value='Germany', duration=-30)
            self.assertNotIn('country', Store._store.keys())
            self.assertIsNone(Store.get('country'))

        def test_clean(self):
            Store.set(key='a', value='A', duration=1)
            Store.set(key='b', value='B', duration=60)
            Store.set(key='c', value='C', duration=1)
            Store.set(key='d', value='D', duration=60)

            self.assertIn('a', Store._store.keys())
            self.assertIn('b', Store._store.keys())
            self.assertIn('c', Store._store.keys())
            self.assertIn('d', Store._store.keys())

            # time.sleep(2)
            # Store.clean()
            #
            # self.assertNotIn('a', Store._store.keys())
            # self.assertIn('b', Store._store.keys())
            # self.assertNotIn('c', Store._store.keys())
            # self.assertIn('d', Store._store.keys())

        def test_purge(self):
            Store.set(key='a', value='A')
            Store.set(key='b', value='B')
            Store.set(key='c', value='C')
            Store.set(key='d', value='D')

            self.assertIn('a', Store._store.keys())
            self.assertIn('b', Store._store.keys())
            self.assertIn('c', Store._store.keys())
            self.assertIn('d', Store._store.keys())

            Store.purge()

            self.assertEqual({}, Store._store)

    unittest.main(verbosity=2)
