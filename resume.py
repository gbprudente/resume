#!/usr/bin/env python
	
class Resume:

    def employment():
        return [
            'Intermediate/Senior',
            'Full-Time',
            'New Countries',
            'New Cultures'
        ]

    def skills():
        return {
                  'Web' : ['Django', 'Flask', 'CSS', 'JQuery', 'Ajax', 'Laravel', 'Git']
                  'Python' : ['numpy', 'scipy', 'biopython', 'twisted', 'telebot', 'simplecv']
                  'Database' : ['SQL', 'PL/SQL']
                  'Open Source' : ['JDownloader-Team member', 'ArchLinux user\'n\'Activist']
                  'Academic' : ['Machine Learning', 'Text Processing']
        }

    def work_experience():
    	return [
    	    {
    	        'Employee' : 'Vaporar'
    	        'Position' : 'Business Management'
    	        'Responsibility' : 'Overseeing purchasing/sales department and creating energy-saving projects on industries'
    	        'When' : 'Sep, 2004 to Sep, 2012'
    	    },
    	    {
                'Employee' : 'IFPE - Instituto Federal de Educação, Ciência e Tecnologia de Pernambuco'
                'Position' : 'Systems Development Coordinator'
    	        'Responsibility' : 'Coordinate systems development at Institute'
    	        'When' : 'Sep, 2012 until now'
    	    }
    	]

    def education():
    	"""Degree: Bachelor of Computer Science
    	University: UFRPE - Universidade Federal Rural de Pernambuco
    	When: Aug, 2010 to Aug, 2016
    	"""
    	return 'www.ufrpe.br'

    def contact():
        info = {
          'name' : 'Ricardo Dantas de Oliveira'
          'mail' : 'licensed at brasnet.org'
          'skype' : 'ricardo__dantas'
          'in' : 'https://www.linkedin.com/in/licensed'
        }