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




st.header("Property Investments",anchor=False)
st.write("\n\n\n")
st.image("property investments.jpg", use_column_width="auto")
st.write("At Real Work Financing Broker CO, our Property Investments service is designed to help you navigate the dynamic real estate market with confidence. We offer expert guidance on identifying lucrative investment opportunities, whether you're looking to buy residential, commercial, or rental properties. Our team conducts thorough market analyses and provides insights into property valuation, financing options, and potential returns, ensuring you make informed decisions.\nWith a focus on maximizing your investment's potential, we tailor our strategies to align with your financial goals, helping you build a diverse and profitable property portfolio.")

st.subheader("Property Investments Categories",anchor=False)
services = [
    {"name": "Home Finance", "desc": "Flexible home financing solutions tailored to help you achieve your dream of homeownership with ease.", "img": "home finance.jpg"},
    {"name": "Mortgage Loans", "desc": "Customized mortgage loan options designed to make your homeownership journey smooth and affordable.", "img": "mortgage loans.jpg"},
    # Add more services here
]

# Function to display services on the main page
def display_services():
    cols = st.columns(3 if st.session_state['is_desktop'] else 1)
    
    for index, service in enumerate(services):
        with cols[index % (3 if st.session_state['is_desktop'] else 1)]:
            st.image(service['img'], use_column_width=True)  # Display service image
            st.subheader(service['name'])
            st.write(service['desc'])
            # Link to the detailed service page
            # st.write(f"[View Details](/{service['name'].lower().replace(' ', '')})", unsafe_allow_html=True)
            st.write(f"[View Details](/{service['name'].replace(' ','_')})", unsafe_allow_html=True)

# Detect screen size (Mobile/Desktop)
if 'is_desktop' not in st.session_state:
    # Assume desktop as default
    st.session_state['is_desktop'] = True

# Show the services
display_services()


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
