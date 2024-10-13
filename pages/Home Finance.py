import streamlit as st

# Set the page configuration to wide layout
st.set_page_config(page_title="Real work Financing Broker CO", layout="wide",initial_sidebar_state='collapsed',page_icon="logo.jpg")

# Hide the three dots menu and Streamlit footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.logo("logo.jpg",icon_image="logo.jpg")

st.image("logo-main.png")
st.write("\n\n\n")



st.header("Home Finance")
st.write("\n\n\n")
st.image("home finance.jpg", use_column_width="auto")
st.write("At Real Work Financing Broker CO, our Home Finance service is designed to assist you in securing the perfect home while ensuring a smooth and stress-free financing experience. We offer a range of mortgage options tailored to meet your individual needs, whether you’re a first-time homebuyer or looking to refinance your existing mortgage.\nOur team of experts will guide you through the entire process, from pre-approval to closing, providing personalized advice and competitive interest rates. With a focus on transparency and customer satisfaction, we strive to make your home financing journey as seamless as possible, helping you achieve your dream of homeownership.")

st.header(":green[Contact Form]")
with st.form("contactform"):
    st.write("Fill the details Below")
    c1,c2=st.columns(2)
    with c1:
        first_name=st.text_input(label="First Name",placeholder="First Name")
    with c2:
        last_name=st.text_input(label="Last Name",placeholder="Last Name")
    c3,c4=st.columns(2)
    with c3:
        phone=st.text_input(label="Phone No.",placeholder="Phone No.")
    with c4:
        email=st.text_input(label="Email",placeholder="Email")
    note=st.text_input(label="Note",placeholder="write your message..")

    submitted=st.form_submit_button("Submit")
    if submitted:
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email="itxabrar7862580@gmail.com"
        reciever_email="investdubai2024@gmail.com"
        password="tpkg yvqp qrlq thai"

        subject=f"New client message!!"
        body=f"Name: {first_name} {last_name}\nEmail: {email}\nPhone: {phone}\n\nUser Note: {note}"

        msg=MIMEMultipart()
        msg["From"]=sender_email
        msg["To"]=reciever_email
        msg["Subject"]=subject
        msg.attach(MIMEText(body,"plain"))

        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        try:
            server.login(sender_email,password)
            server.sendmail(sender_email,reciever_email,msg.as_string())
            st.success("Thanks, Our team will contact you soon!!")
        except:
            pass
        finally:
            server.quit()
        


st.write("\n\n\n\n\n\n\n\n")

st.header(":green[Visit US]",anchor=False)


st.write("🏢 Burjuman Business Tower, 20 Floor-2058 Al Mankool, Bur Dubai U.A.E")

st.write("☎ +971 4 2588721")

st.text("📩 ptigroup-ae@outlook.com")

st.write("[📞 Whatsapp Us](https://wa.me/971042588721)")
st.write("\n\n\n")

    

# Back to main services page
if st.button("Go back to services"):
    st.write("[Back to Services](/)", unsafe_allow_html=True)
