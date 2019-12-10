from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):
    """
    handles neccessary test required for CustomUser model
    """
    
    def setUp(self):
        self.john_user = get_user_model().objects.create(
            username = 'johndoe',
            email = 'johndoe@gmail.com',
        )
        self.john_user.set_password("johndoepass")


        self.jane_user = get_user_model().objects.create(
            username = 'janedoe',
            email = 'janedoe@gmail.com',
        )
        self.jane_user.set_password("janedoepass")



    def test_user_account_create_with_valid_data(self):
        """
        when valid data are inputted to create an account, then
        the account should be created successfully with the valid data
        """
        # check for john user
        self.assertEqual(self.john_user.username, "johndoe")
        self.assertEqual(self.john_user.email, "johndoe@gmail.com")
        self.assertTrue(self.john_user.check_password("johndoepass"))

        # check for jane user
        self.assertEqual(self.jane_user.username, "janedoe")
        self.assertEqual(self.jane_user.email, "janedoe@gmail.com")
        self.assertTrue(self.jane_user.check_password("janedoepass"))

    
    def test_invalid_user_password_on_password_check(self):
        """
        when an invalid password is passed for a user, test should fail
        """
        # check for jane
        self.assertFalse(self.jane_user.check_password("janedoepassword"))
        # check for john
        self.assertFalse(self.john_user.check_password("johndoepassword"))

    
    def test_no_two_or_more_user_account_can_be_the_same(self):
        """
        no two user account can be the same
        """
        self.assertNotEqual(self.john_user, self.jane_user)
