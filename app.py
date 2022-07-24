import streamlit as st

def main():
    st.title("""Multiplication of 2 numbers""")

    one=st.number_input("First_Number")
    two=st.number_input("Second number")

    ans=one*two

    st.write(one,"X",two,"=",ans)


if __name__ == '__main__':
    main()
