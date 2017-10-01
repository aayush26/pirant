import unittest
import colander
import pirant.models


class NewsTest(unittest.TestCase):
    """
    Unit tests for the News class model
    """

    def setUp(self):
        self.news = pirant.models.News()
        self.data = {
            'id': 123,
            'type': 'T',
            'headline': 'MyHeadline',
            'body': 'MyBody',
            'footer': 'MyFooter',
            'height': 456,
            'action': 'MyAction'
        }

    def test_happyCaseDeserializeNews(self):
        deserialized = self.news.deserialize(self.data)
        assert deserialized['id'] == 123
        assert deserialized['type'] == 'T'
        assert deserialized['headline'] == 'MyHeadline'
        assert deserialized['body'] == 'MyBody'
        assert deserialized['footer'] == 'MyFooter'
        assert deserialized['height'] == 456
        assert deserialized['action'] == 'MyAction'

    def test_idMustBeInt(self):
        self.data['id'] = 'NotANumber'
        with self.assertRaises(colander.Invalid):
            self.news.deserialize(self.data)

    def test_typeMustBeString(self):
        self.data['type'] = 1
        with self.assertRaises(colander.Invalid):
            self.news.deserialize(self.data)

    def test_heightMustBeInt(self):
        self.data['height'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.news.deserialize(self.data)


class RantTest(unittest.TestCase):
    """
    Unit tests for the Rant class model
    """

    def setUp(self):
        self.rant = pirant.models.Rant()
        self.data = {
            'id': 1,
            'text': 'Txt',
            'score': 111,
            'created_time': 234432,
            'user_id': 43289,
            'num_comments': 121,
            'user_username': 'user'
        }

    def test_happyCaseDeserializeRant(self):
        deserialized = self.rant.deserialize(self.data)
        assert deserialized['id'] == 1

    def test_idMustBeInt(self):
        self.data['id'] = 'NotANumber'
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.data)

    def test_textMustBeString(self):
        self.data['text'] = 1
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.data)

    def test_scoreMustBeInt(self):
        self.data['score'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.data)

    def test_created_timeMustBeInt(self):
        self.data['created_time'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.data)

    def test_user_idMustBeInt(self):
        self.data['user_id'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.data)

    def test_num_commentsMustBeInt(self):
        self.data['num_comments'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.data)

    def test_user_usernameMustBeString(self):
        self.data['user_username'] = 1
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.data)


class RantResponseTest(unittest.TestCase):
    """
    Unit tests for the RantResponse class model
    """

    def setUp(self):
        self.rants_response = pirant.models.RantsResponse()
        self.data = {
            'rants': [{
                    'id': 1234,
                    'text': 'Txt',
                    'score': 111,
                    'created_time': 234432,
                    'user_id': 43289,
                    'num_comments': 121,
                    'user_username': 'user'
            }],
            'news': {
                'id': 123,
                'type': 'T',
                'headline': 'MyHeadline',
                'body': 'MyBody',
                'footer': 'MyFooter',
                'height': 456,
                'action': 'MyAction'
            },
            'success': True,
            'set': '1',
            'wrw': 1
        }

    def test_happyCaseDeserializeRantResponse(self):
        deserialized = self.rants_response.deserialize(self.data)
        assert deserialized['rants'][0]['id'] == 1234
