import streamlit as st

def check_credentials(username, password):
    # ตรวจสอบข้อมูลในฐานข้อมูล (ตัวอย่าง)
    if username == "win" and password == "win":
        return True
    else:
        return False

def main():
    st.title("Login Program")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        username = st.text_input("User")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if check_credentials(username, password):
                st.session_state.logged_in = True
                st.success("Login สำเร็จ")
                
            else:
                st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
                
    else:
        
            

if __name__ == "__main__":
    main()
