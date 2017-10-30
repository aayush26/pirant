from __future__ import absolute_import, division, print_function
import unittest
import colander
import pirant.models


class NewsTest(unittest.TestCase):
    """
    Unit tests for the News class model
    """

    def setUp(self):
        self.news = pirant.models.News()
        self.test_data = {
            'id': 123,
            'type': 'T',
            'headline': 'MyHeadline',
            'body': 'MyBody',
            'footer': 'MyFooter',
            'height': 456,
            'action': 'MyAction'
        }

    def test_happyCaseDeserializeNews(self):
        deserialized = self.news.deserialize(self.test_data)
        assert deserialized['id'] == 123
        assert deserialized['type'] == 'T'
        assert deserialized['headline'] == 'MyHeadline'
        assert deserialized['body'] == 'MyBody'
        assert deserialized['footer'] == 'MyFooter'
        assert deserialized['height'] == 456
        assert deserialized['action'] == 'MyAction'

    def test_idMustBeInt(self):
        self.test_data['id'] = 'NotANumber'
        with self.assertRaises(colander.Invalid):
            self.news.deserialize(self.test_data)

    def test_typeMustBeString(self):
        self.test_data['type'] = 1
        with self.assertRaises(colander.Invalid):
            self.news.deserialize(self.test_data)

    def test_heightMustBeInt(self):
        self.test_data['height'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.news.deserialize(self.test_data)


class RantTest(unittest.TestCase):
    """
    Unit tests for the Rant class model
    """

    def setUp(self):
        self.rant = pirant.models.Rant()
        self.test_data = {
            'id': 1,
            'text': 'Txt',
            'score': 111,
            'created_time': 234432,
            'user_id': 43289,
            'num_comments': 121,
            'user_username': 'user',
            'upvotes': 2,
            'downvotes': 0,
            'user_userscore': 300,
            'attachedImage': {
                'url': 'https://test.devrant.com/',
                'width': 20,
                'height': 30
            },
            'tags': ['Devrant', 'devrant']
        }

    def test_happyCaseDeserializeRant(self):
        deserialized = self.rant.deserialize(self.test_data)
        assert deserialized['id'] == 1

    def test_idMustBeInt(self):
        self.test_data['id'] = 'NotANumber'
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.test_data)

    def test_textMustBeString(self):
        self.test_data['text'] = 1
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.test_data)

    def test_scoreMustBeInt(self):
        self.test_data['score'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.test_data)

    def test_created_timeMustBeInt(self):
        self.test_data['created_time'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.test_data)

    def test_user_idMustBeInt(self):
        self.test_data['user_id'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.test_data)

    def test_num_commentsMustBeInt(self):
        self.test_data['num_comments'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.test_data)

    def test_user_usernameMustBeString(self):
        self.test_data['user_username'] = 1
        with self.assertRaises(colander.Invalid):
            self.rant.deserialize(self.test_data)


class RantsResponseTest(unittest.TestCase):
    """
    Unit tests for the RantsResponse class model
    """

    def setUp(self):
        self.rants_response = pirant.models.RantsResponse()
        self.test_data = {
            'rants': [{
                'id': 1234,
                'text': 'Txt',
                'score': 111,
                'created_time': 234432,
                'user_id': 43289,
                'num_comments': 121,
                'user_username': 'user',
                'upvotes': 2,
                'downvotes': 0,
                'user_userscore': 300,
                'attachedImage': {
                    'url': 'https://test.devrant.com/',
                    'width': 20,
                    'height': 30
                },
                'tags': ['Devrant', 'devrant']
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
        deserialized = self.rants_response.deserialize(self.test_data)
        assert deserialized['rants'][0]['id'] == 1234

class CommentTest(unittest.TestCase):
    """
    Unit tests for the Comment class model
    """

    def setUp(self):
        self.comment = pirant.models.Comment()
        self.test_data = {
            'id': 1234,
            'rant_id': 2345,
            'body': 'test body',
            'upvotes': 2,
            'downvotes': 1,
            'score': 10,
            'created_time': 20102313123,
            'user_id': 111,
            'user_username': 'testUser',
            'user_userscore': 56
        }

    def test_happyCaseDeserializeComment(self):
        deserialized = self.comment.deserialize(self.test_data)
        assert deserialized['id'] == 1234
        assert deserialized['user_username'] == 'testUser'

    def test_idMustBeInt(self):
        self.test_data['id'] = 'NotANumber'
        with self.assertRaises(colander.Invalid):
            self.comment.deserialize(self.test_data)

    def test_rantIdMustBeInt(self):
        self.test_data['rant_id'] = 'NotANumber'
        with self.assertRaises(colander.Invalid):
            self.comment.deserialize(self.test_data)

    def test_bodyMustBeString(self):
        self.test_data['body'] = 1
        with self.assertRaises(colander.Invalid):
            self.comment.deserialize(self.test_data)

    def test_upvotesMustBeInt(self):
        self.test_data['upvotes'] = 'NotANumber'
        with self.assertRaises(colander.Invalid):
            self.comment.deserialize(self.test_data)

    def test_downvotesMustBeInt(self):
        self.test_data['downvotes'] = 'NotANumber'
        with self.assertRaises(colander.Invalid):
            self.comment.deserialize(self.test_data)

    def test_scoreMustBeInt(self):
        self.test_data['score'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.comment.deserialize(self.test_data)

    def test_created_timeMustBeInt(self):
        self.test_data['created_time'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.comment.deserialize(self.test_data)

    def test_user_idMustBeInt(self):
        self.test_data['user_id'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.comment.deserialize(self.test_data)

    def test_user_usernameMustBeString(self):
        self.test_data['user_username'] = 1
        with self.assertRaises(colander.Invalid):
            self.comment.deserialize(self.test_data)

    def test_user_scoreMustBeInt(self):
        self.test_data['user_userscore'] = 'nan'
        with self.assertRaises(colander.Invalid):
            self.comment.deserialize(self.test_data)


class CommentsTest(unittest.TestCase):
    """
    Unit tests for the Comments class model
    """

    def setUp(self):
        self.comments = pirant.models.Comments()
        self.test_data = [{
            'id': 1234,
            'rant_id': 2345,
            'body': 'test body',
            'upvotes': 2,
            'downvotes': 1,
            'score': 10,
            'created_time': 20102313123,
            'user_id': 111,
            'user_username': 'testUser',
            'user_userscore': 56
        }]

    def test_happyCaseDeserializeComments(self):
        deserialized = self.comments.deserialize(self.test_data)
        assert deserialized[0]['id'] == 1234
        assert deserialized[0]['body'] == 'test body'


class RantResponseTest(unittest.TestCase):
    """
    Unit tests for the RantResponse class model
    """

    def setUp(self):
        self.rantResponse = pirant.models.RantResponse()
        self.test_data = {
            'rant': {
                'id': 1234,
                'text': 'Txt',
                'score': 111,
                'created_time': 234432,
                'user_id': 43289,
                'num_comments': 121,
                'user_username': 'user',
                'upvotes': 2,
                'downvotes': 0,
                'user_userscore': 300,
                'attachedImage': {
                    'url': 'https://test.devrant.com/',
                    'width': 20,
                    'height': 30
                },
                'tags': ['Devrant', 'devrant']
            },
            'comments': [{
                'id': 1234,
                'rant_id': 2345,
                'body': 'test body',
                'upvotes': 2,
                'downvotes': 1,
                'score': 10,
                'created_time': 20102313123,
                'user_id': 111,
                'user_username': 'testUser',
                'user_userscore': 56
            }],
            'success': True
        }

    def test_happyCaseDeserializeRantResponse(self):
        deserialized = self.rantResponse.deserialize(self.test_data)
        assert deserialized['rant']['id'] == 1234
        assert deserialized['comments'][0]['user_id'] == 111
        assert deserialized['success'] == True
