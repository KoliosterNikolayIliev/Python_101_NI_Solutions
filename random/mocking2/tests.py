from unittest import TestCase
from unittest.mock import patch

from main import main


class TestMain(TestCase):

    @patch('main.list_users')
    @patch('main.create_user')
    @patch('main.unknown_command')
    @patch('main.help')
    @patch('main.input')
    def test_help_function_is_called_if_command_is_h(
        self,
        input_mock,
        help_mock,
        unknown_command_mock,
        create_user_mock,
        list_users_mock
    ):
        input_mock.side_effect = ['h', 'e']

        main()

        help_mock.assert_called_once_with()

        self.assertFalse(unknown_command_mock.called)
        self.assertFalse(list_users_mock.called)
        self.assertFalse(create_user_mock.called)

    @patch('main.list_users')
    @patch('main.create_user')
    @patch('main.unknown_command')
    @patch('main.help')
    @patch('main.input')
    def test_help_function_is_called_if_command_is_help(
        self,
        input_mock,
        help_mock,
        unknown_command_mock,
        create_user_mock,
        list_users_mock
    ):
        input_mock.side_effect = ['help', 'e']

        main()

        help_mock.assert_called_once_with()

        self.assertFalse(unknown_command_mock.called)
        self.assertFalse(list_users_mock.called)
        self.assertFalse(create_user_mock.called)


"""
....................
"""

from unittest import TestCase
from unittest.mock import patch, MagicMock
from main import create_user


class CreateUserTests(TestCase):
    @patch('main.json')
    @patch('main.open')
    @patch('main.fetch_users')
    @patch('main.input')
    def test_create_user(
        self,
        input_mock,
        fetch_users_mock,
        open_mock,
        json_mock
    ):
        first_name, last_name = 'Ivo', 'Donchev'
        input_mock.side_effect = [first_name, last_name]

        create_user()

        fetch_users_mock.return_value.append.assert_called_once_with(
            {
                'first_name': first_name,
                'last_name': last_name
            }
        )
        f_mock = open_mock.return_value.__enter__.return_value
        f.write.assert_called_once_with(json_mock.dumps.return_value)
        json_mock.dumps.assert_called_once_with(fetch_users_mock.return_value)