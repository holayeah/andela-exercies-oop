import unittest

class PersonTestCase(unittest.TestCase):
    """
    Tests for the person class
    """
    
    def test_person_is_created(self):
        """
        tests for creating a person 
        """
        p = Person('firstname', 'lastname', [1, 1, 2016])
        self.assertEqual(p.first_name, 'first_name')
        self.assertEqual(p.last_name, 'last_name')
        self.assertEqual(p.age(), 1)

    def test_defaults(self):
        """
        Test if the birthday is set to default
        """
        p = Person('firstname', 'lastname')
        self.assertEqual(p.age(), 0)


class DoctorTestCase(unittest.TestCase):
    """
    Testing a doctor class child of person 
    """
 
    def setUp(self):
        
        self.oldd = Doctor('firstname', 'lastname', bithday=[1, 1, 1956], start_career=[1, 1, 1986])
        self.youngd = Doctor('youngfirstname', 'younglastname', birthday=[1, 1, 1986], start_career=[1, 1, 2016])

    def test_doctor_is_created(self):
        """
        tests for creating a doctro
        """
        self.assertEqual(d.first_name, 'first_name')
        self.assertEqual(d.last_name, 'last_name')
        self.assertEqual(d.age, 61)
        self.assertEqual(d.experience, 31)

   def test_can_retire(self):
       """
       Tests if the doctor can be allowed to retire
       """
       self.assertTrue(self.oldd.can_retire())
       self.assertFalse(self.youngd.can_retire())
