#! /usr/bin/python3.7

from classes.jenkins import selenium

if __name__ == "__main__":
    
    init = selenium()
    """
    groupPolicy ---> view in config file config/jenkins_group_access.yml
    """
    username    = 'test'
    password    = 't4too7a'
    first_name  = 'Test'
    last_name   = 'Testtovich'
    email       = 'ttestovich@example.com'
    groupPolicy = 'platform'

    init.user_create(username   = username, 
                     password   = password, 
                     first_name = first_name,
                     last_name  = last_name,
                     groupPolicy= groupPolicy)

    init.user_delete(username)
    init.browser_close()
