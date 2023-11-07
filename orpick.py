import streamlit as st

st.sidebar.title("Orpick Music Band Studio")

st.write ("Kindly chose your options on left sidebar")

if st.sidebar.button("Student Registration"):
    st.title("Student Registration")
    st.write("Kindly fill this if you want to learn Music from Orpick Studios  \n[Student Registration Form](https://forms.gle/FAVrsh2XoCFrD4a78)")
if st.sidebar.button("Event Inquiry"):
    st.title("Event inquiry")
    st.write("Fill this form if you want to book Musicians for your next Event  \n[Event Inquiry](https://forms.gle/2uNpUCSdYJJS42f48)")
if st.sidebar.button("About Me"):
    st.title("About Me")
    st.write('Meet Iqbal Warsi, a maestro in the realm of music, whose passion for sonic artistry has led him to establish the renowned music studio, Orpick. With a rich musical background and an unwavering dedication to his craft, Iqbal has become a luminary figure in the industry.   \n\nFor the past 15 years, he has not only honed his own musical prowess but has also imparted his knowledge and expertise to countless aspiring musicians. As the proud owner of Orpick, Iqbal provides a nurturing space for creativity to flourish. His commitment to cultivating talent is reflected in the success stories of the students who have passed through the doors of his studio, making Orpick a beacon for those seeking to master the harmonies of the musical world.')
if st.sidebar.button("Contact us"):
    st.title("Contact us")
    st.write("Lal Kothi , Roshnara Road  \n"
             "Orpick Music Studio  \n"
             "New Delhi 110007  \n"
             "Near Pulbangash Metro Station  \n"
             "...................  \n"
             "Mobile 1234567890  \n"
             "Asistant manager 0987654321  \n"
              "...................  \n"

             "Email ID : orpick@gmail.com  \n"


             "For musical comedy videos Contact  \n"
             "Email ID : rightorwrongmusic@gmail.com"
             )
