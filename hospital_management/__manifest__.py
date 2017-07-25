# -*- coding: utf-8 -*-


{
    'name': 'Hospital Management',
    'version': '10.0.1.0.1',
    'category': 'Hospital',
    
    'depends': [
        'base',
    ],
   
    
    'data': [
        'views/doctorallcategory.xml',
        'views/patientallcategory.xml',
        'views/facilityallcategory.xml',
        'views/report_action.xml',
        'views/report_patient_view.xml',
    ],
    
    'installable': True,
    'application': True,
}
