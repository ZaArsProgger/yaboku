from django.test import TestCase

from .models import Message

# Create your tests here.

class QuestionMethodTests(TestCase):

    def test_was_message_length_must_be_no_short(self):
        flood_message = Message(message='spam')
        self.assertEqual(flood_message.is_fine_message(), False)
