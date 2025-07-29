import streamlit as st
import pandas as pd

def check_credentials(username, password):
    try:
        df = pd.read_excel('main/users.xlsx')  # ตรวจสอบ path
        user_match = df[(df['username'] == username) & (df['password'] == password)]
        return not user_match.empty
    except FileNotFoundError:
        st.error("ไม่พบไฟล์ users.xlsx")
        return False
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {str(e)}")
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
                st.session_state.username = username
                st.success("Login สำเร็จ")
                st.rerun()
            else:
                st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    else:
        st.write(f"ยินดีต้อนรับ {st.session_state.username}!")
        options = ["ตัวเลือก 1", "ตัวเลือก 2", "ตัวเลือก 3"]
        selected_option = st.selectbox("กรุณาเลือกตัวเลือก:", options)
        
        if selected_option:
            st.write(f"คุณเลือก: {selected_option}")
        
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()

if __name__ == "__main__":
    main()
