from collections import namedtuple


setting_nt = namedtuple('Setting', 'vietnamese english')
sett_level_nt = namedtuple('SettingLevel', 'vietnamese english level')
emp_contract_nt = namedtuple('EmpContract', 'vietnamese english is_full_time')

RELIGION = (
    setting_nt('Không', 'None'),
    setting_nt('Phật giáo', 'Buddhism'),
    setting_nt('Công giáo', 'Catholicism'),
    setting_nt('Tin Lành', 'Protestantism'),
    setting_nt('Hồi giáo', 'Islam'),
    setting_nt('Khác', 'Other'),
)

WORKING_STATUS = (
    setting_nt('Thử việc', 'Probation'),
    setting_nt('Đang làm việc', 'Working'),
    setting_nt('Nghỉ không lương', 'Unpaid Leave'),
    setting_nt('Nghỉ thai sản', 'Maternity Leave'),
    setting_nt('Nghỉ bệnh', 'Sick Leave'),
    setting_nt('Đi học tập trung', 'Studying Mode'),
    setting_nt('Nghỉ việc', 'Leave'),
    setting_nt('Nghỉ hưu', 'Retirement'),
)

EMPLOYMENT_CONTRACT = (
    emp_contract_nt('HĐLĐ 1 năm', '1-year contract', True),
    emp_contract_nt('HĐLĐ 3 năm', '3-year contract', True),
    emp_contract_nt('HĐLĐ vô thời hạn', 'Permanent contract', True),
    emp_contract_nt('HĐ Cộng tác viên', 'Part-time contract', False),
    emp_contract_nt('HĐ Tư vấn', 'Consultant contract', False),
)

TEACHING_TITLE = (
    sett_level_nt('Trợ giảng 1', 'Teaching Assistant 1', 1),
    sett_level_nt('Trợ giảng 2', 'Teaching Assistant 2', 2),
    sett_level_nt('Giảng viên', 'Lecturer 1', 3),
    sett_level_nt('Giảng viên chính', 'Lecturer 2', 4),
    sett_level_nt('Giảng viên cao cấp', 'Senior Lecturer', 5),
    sett_level_nt('Nhà giáo ưu tú', 'Meritous Teacher', 6),
    sett_level_nt('Nhà giáo nhân dân', 'National Teacher', 7),
)

ACADEMIC_TITLE = (
    sett_level_nt('Giáo Sư', 'Professor', 2),
    sett_level_nt('Phó Giáo Sư', 'Associate Professor', 1),
)

DEGREE = (
    sett_level_nt('Cử nhân', 'Bachelor', 7),
    sett_level_nt('Kỹ sư', 'Engineer', 7),
    sett_level_nt('Bác sỹ', 'Medical Doctor', 7),
    sett_level_nt('Thạc sỹ', 'Master', 8),
    sett_level_nt('Tiến sỹ', 'PhD', 9),
    sett_level_nt('Tiến sỹ QTKD', 'DBA', 9)
)

TRAINING_LEVEL = (
    sett_level_nt('Tú Tài', 'Baccalaureate', 4),
    sett_level_nt('Trung Cấp', 'Vocational Certificate', 5),
    sett_level_nt('Cao Đẳng', 'Associate Degree', 6),
    sett_level_nt('Đại Học', 'Bachelor', 7),
    sett_level_nt('Thạc Sỹ', 'Master', 8),
    sett_level_nt('Tiến Sỹ', 'Doctor', 9)
)

TITLE = (
    sett_level_nt('Chủ tịch', 'Chairman', 1),
    sett_level_nt('Phó chủ tịch', 'Vice Chairman', 2),
    sett_level_nt('Hiệu Trưởng', 'President', 2),
    sett_level_nt('Thường trực HĐQT', 'Executive Member', 3),
    sett_level_nt('Phó Hiệu Trưởng Thường Trực', 'Standing Vice President', 3),
    sett_level_nt('Phó Hiệu Trưởng', 'Vice President', 4),
    sett_level_nt('Tổng Giám Đốc', 'CEO', 3),
    sett_level_nt('Giám Đốc Tài Chính', 'CFO', 4),
    sett_level_nt('Giám Đốc', 'Director', 5),
    sett_level_nt('Phó Giám Đốc', 'Deputy Director', 6),
    sett_level_nt('Trưởng Đơn Vị', 'Head', 5),
    sett_level_nt('Quyền Trưởng Đơn Vị', 'Acting Head', 6),
    sett_level_nt('Phó Trưởng Đơn Vị', 'Deputy Head', 6),
    sett_level_nt('Trưởng Khoa', 'Dean', 5),
    sett_level_nt('Quyền Trưởng Khoa', 'Acting Dean', 6),
    sett_level_nt('Phó Trưởng Khoa', 'Vice Dean', 6),
    sett_level_nt('Chánh Văn Phòng', 'Chief of Staff', 5),
    sett_level_nt('Tổng Biên Tập', 'Chief Editor', 5),
    sett_level_nt('Giảng Viên', 'Lecturer', 7),
    sett_level_nt('Nghiên Cứu Viên', 'Researcher', 7),
    sett_level_nt('Chuyên Viên', 'Expert', 7),
    sett_level_nt('Nhân Viên', 'Staff', 7),
    sett_level_nt('Cộng Tác Viên', 'Collaborator', 8),
    sett_level_nt('Thực tập sinh', 'Intern', 8),
    sett_level_nt('Thành Viên', 'Member', 8),
    sett_level_nt('Cố Vấn', 'Consultant', 8),
    sett_level_nt('Kế Toán Trưởng', 'Chief Accountant', 5),
)
