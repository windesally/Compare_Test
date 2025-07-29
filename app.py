import streamlit as st

def check_credentials(username, password):
    # ตรวจสอบข้อมูลในฐานข้อมูล (ตัวอย่าง)
    if username == "win" and password == "win":
        return True
    else:
        return False

def print():
    st.write("Hello")


def main():
@@ -25,13 +23,13 @@
                st.session_state.logged_in = True
                st.success("Login สำเร็จ")
                st.rerun()
                print()



            else:
                st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    else:
        return

if __name__ == "__main__":
    main()
