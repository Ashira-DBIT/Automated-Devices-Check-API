🇺🇸 English (International)

About the Project :



Drawbridge Sentinel is a lightweight open-source tool designed to bridge the gap between physical and cyber security monitoring. It monitors network devices (e.g., CCTV cameras, access control systems) and automatically triggers alerts via the LINE Messaging API when a device goes offline.



Key Features :



Continuous Monitoring: Automatically scans device status at set intervals.

Proactive Alerts: Sends immediate notifications to a private LINE Official Account.

Security Conscious: Utilizes environment variables to keep credentials safe.

Developer Friendly: Easy to configure and ready for professional deployment.



Getting Started :

\- Install dependencies: pip install python-dotenv



\- Create a .env file with your LINE\_ACCESS\_TOKEN and USER\_ID.



\- Add your device IPs to the devices dictionary in check\_devices.py.



\- Execute the script: python check\_devices.py


 🇹🇭 ฉบับภาษาไทย (Thai)

เกี่ยวกับโปรเจกต์


Drawbridge Sentinel คือเครื่องมือ Open Source ที่ออกแบบมาเพื่อยกระดับความปลอดภัยให้กับอุปกรณ์ในเครือข่าย (เช่น กล้องวงจรปิด, ระบบควบคุมประตู) โดยเน้นความง่ายและรวดเร็ว ระบบจะทำการตรวจสอบสถานะอุปกรณ์ (Device Health Check) โดยอัตโนมัติ และแจ้งเตือนทันทีผ่าน LINE Messaging API เมื่อตรวจพบความผิดปกติ



คุณสมบัติ :

Automation: ตรวจสอบสถานะอุปกรณ์ซ้ำอัตโนมัติตามช่วงเวลาที่กำหนด
Instant Alert: แจ้งเตือนเข้าสู่ LINE OA ส่วนตัวทันทีเมื่ออุปกรณ์ Offline
Security First: มีการแยกจัดการรหัสลับ (Secrets) ออกจากโค้ดหลักเพื่อความปลอดภัย
Lightweight: ทำงานได้รวดเร็วและใช้ทรัพยากรเครื่องน้อย





วิธีการใช้งานเบื้องต้น :
ติดตั้ง Library: pip install python-dotenv
-สร้างไฟล์ .env และระบุ LINE\_ACCESS\_TOKEN และ USER\_ID
-ระบุ IP ของอุปกรณ์ที่ต้องการเฝ้าระวังในไฟล์ DBSN.py
-รันโปรแกรมด้วยคำสั่ง: python DBSN.py

