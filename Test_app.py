from app import app
import unittest 

class FlaskFSSTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_home_status_code(self):
        result = self.app.get('/') 

        self.assertEqual(result.status_code, 200) 

    def test_home_data(self):
        result = self.app.get('/',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))

    def test_about_status_code(self):
        result = self.app.get('/about') 

        self.assertEqual(result.status_code, 200) 

    def test_about_data(self):
        result = self.app.get('/about',content_type = 'text/html') 
        
        #print(result.data.decode('utf-8'))
        self.assertIn("Hello Joe", result.data.decode('utf-8'))
        
    def test_login_status_code(self):
        result = self.app.get('/login') 

        self.assertEqual(result.status_code, 200) 
        
    def test_login_data(self):
        result = self.app.get('/login',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))

    def test_register_status_code(self):
        result = self.app.get('/register') 

        self.assertEqual(result.status_code, 200) 
        
    def test_register_data(self):
        result = self.app.get('/register',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_index_status_code(self):
        result = self.app.get('/index') 

        self.assertEqual(result.status_code, 200) 
        
    def test_index_data(self):
        result = self.app.get('/index',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_profile_status_code(self):
        result = self.app.get('/profile') 

        self.assertEqual(result.status_code, 200) 
        
    def test_profile_data(self):
        result = self.app.get('/profile',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_viewprofile_status_code(self):
        result = self.app.get('/viewprofile') 

        self.assertEqual(result.status_code, 200) 
        
    def test_viewprofile_data(self):
        result = self.app.get('/viewprofile',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_upload_status_code(self):
        result = self.app.get('/upload') 

        self.assertEqual(result.status_code, 200) 
        
    def test_upload_data(self):
        result = self.app.get('/upload',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_viewupload_status_code(self):
        result = self.app.get('/viewupload') 

        self.assertEqual(result.status_code, 200) 
        
    def test_viewupload_data(self):
        result = self.app.get('/viewupload',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_publications_status_code(self):
        result = self.app.get('/publications') 

        self.assertEqual(result.status_code, 200) 
        
    def test_publications_data(self):
        result = self.app.get('/publications',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_fdp_status_code(self):
        result = self.app.get('/fdp') 

        self.assertEqual(result.status_code, 200) 
        
    def test_fdp_data(self):
        result = self.app.get('/fdp',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_mycas_status_code(self):
        result = self.app.get('/mycas') 

        self.assertEqual(result.status_code, 200) 
        
    def test_mycas_data(self):
        result = self.app.get('/mycas',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_changepassword_status_code(self):
        result = self.app.get('/changepassword') 

        self.assertEqual(result.status_code, 200) 
        
    def test_changepassword_data(self):
        result = self.app.get('/changepassword',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_loginspecial_status_code(self):
        result = self.app.get('/loginspecial') 

        self.assertEqual(result.status_code, 200) 
        
    def test_loginspecial_data(self):
        result = self.app.get('/loginspecial',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_addhod_status_code(self):
        result = self.app.get('/addhod') 

        self.assertEqual(result.status_code, 200) 
        
    def test_addhod_data(self):
        result = self.app.get('/addhod',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_deletehod_status_code(self):
        result = self.app.get('/deletehod') 

        self.assertEqual(result.status_code, 200) 
        
    def test_deletehod_data(self):
        result = self.app.get('/deletehod',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_addfaculty_status_code(self):
        result = self.app.get('/addfaculty') 

        self.assertEqual(result.status_code, 200) 
        
    def test_addfaculty_data(self):
        result = self.app.get('/addfaculty',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_viewfaculty_status_code(self):
        result = self.app.get('/viewfaculty') 

        self.assertEqual(result.status_code, 200) 
        
    def test_viewfaculty_data(self):
        result = self.app.get('/viewfaculty',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_cas_status_code(self):
        result = self.app.get('/cas') 

        self.assertEqual(result.status_code, 200) 
        
    def test_cas_data(self):
        result = self.app.get('/cas',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))
        
    def test_hod_status_code(self):
        result = self.app.get('/hod') 

        self.assertEqual(result.status_code, 200) 
        
    def test_hod_data(self):
        result = self.app.get('/hod',content_type = 'text/html') 

        #print(result.data.decode('utf-8'))
        self.assertIn("FACULTY FACILITATION SYSTEM", result.data.decode('utf-8'))