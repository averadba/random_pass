import streamlit as st
import random
import string

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse', False)

def generate_password(length, exclude_chars):
    """
    Generate a random password of the specified length.
    """
    exclude_chars = exclude_chars + "(){}[]|`¬¦!\"£$%^&*,=+<>;' " # adding characters that should be excluded by default
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # remove excluded characters from the character set
    for char in exclude_chars:
        all_chars = all_chars.replace(char, '')
    # generate the password
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

st.title("Random Password Generator")
st.write("By: A. Vera")

length = st.slider("Select the length of the password", 8, 32, 12)
exclude_chars = st.text_input("Exclude special characters (comma separated)")

if st.button("Generate Password"):
    if len(exclude_chars) >= length:
        st.error("Number of excluded characters should be less than the total length of the password")
    else:
        password = generate_password(length, exclude_chars)
        st.success(f"Generated Password: {password}")
