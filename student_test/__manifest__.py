{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'ระบบจัดการข้อมูลนักเรียน',
    'description': """
        โมดูลจัดการข้อมูลนักเรียน ซึ่งประกอบด้วย:
        - ข้อมูลพื้นฐาน
        - คำนำหน้า
        - ชื่อนักเรียน (ไม่ซ้ำกัน)
        - วันเกิดและการคำนวณอายุอัตโนมัติ
    """,
    'category': 'Education',
    'author': 'Your Name',
    'depends': ['base', 'mail', 'sale_management'],
    'data': [
        'security/groups.xml',
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/title_view.xml',
        'views/student_view.xml',
        'views/teacher_action.xml',
        'views/subject_action.xml',
        'views/district_view.xml',
        'views/postcode_view.xml',
        'views/province_view.xml',
        'views/sub_district_view.xml',
        'views/sale_order_view.xml',
        'views/menu_view.xml',
        'report/report_grade.xml'
    ],

    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}