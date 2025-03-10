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
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/title_view.xml',
        'views/student_view.xml',
        'views/teacher_action.xml',
        'views/district_view.xml',
        'views/postcode_view.xml',
        'views/province_view.xml',
        'views/sub_district_view.xml',
        'views/sale_order_view.xml',
        'views/menu_view.xml'
    ],

    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}