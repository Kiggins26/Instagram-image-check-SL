import streamlit as st
from modelHelper import judge_image

st.write("""
        # Instagram image judge
        using ml to pick the image that will do the best on instagram
""")

image_files = st.file_uploader("Pick your images", type = ['png','jpeg','jpg'], accept_multiple_files=True)

if image_files is not None:

    image_score_pairs = {}

    for image_file in image_files:
        image_score = float(judge_image(image_file))
        image_score_pairs[image_file] = image_score
    
    image_score_pairs = dict(sorted(image_score_pairs.items(), key = lambda item: item[1]))
    
    
    st.write("""
            ### The images below are ordered from best to worst in terms of like prediction
            """)

    for image in reversed(image_score_pairs):

        st.image(image, caption = image_score_pairs[image]) 
